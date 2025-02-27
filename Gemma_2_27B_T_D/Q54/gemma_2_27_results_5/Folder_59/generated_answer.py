def all_right_truncatable_prime(nums):
    x = nums[84]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_truncatable = True
            n = str(i)
            while len(n) > 0:
                if not is_prime(int(n)):
                    is_truncatable = False
                    break
                n = n[:-1]
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True