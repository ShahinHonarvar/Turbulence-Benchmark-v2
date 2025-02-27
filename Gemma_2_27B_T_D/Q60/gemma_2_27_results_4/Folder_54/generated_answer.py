def all_left_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        if '0' in str(num):
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            is_truncatable = True
            n = str(num)
            while len(n) > 1:
                n = n[1:]
                if not prime_check(int(n)):
                    is_truncatable = False
                    break
            n = str(num)
            while len(n) > 1:
                n = n[:-1]
                if not prime_check(int(n)):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def prime_check(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True