def all_right_truncatable_prime(nums):
    x = nums[645]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            truncatable = True
            n = str(i)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True