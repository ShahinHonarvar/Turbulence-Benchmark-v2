def all_left_right_truncatable_prime(nums):
    x = nums[20]
    primes = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and '0' not in str(i):
            truncatable = True
            n = str(i)
            while len(n) > 1:
                n = n[1:]
                if not is_prime_number(int(n)):
                    truncatable = False
                    break
            n = str(i)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime_number(int(n)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True