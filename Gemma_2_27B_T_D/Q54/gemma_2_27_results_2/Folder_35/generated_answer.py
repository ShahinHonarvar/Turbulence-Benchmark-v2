def all_right_truncatable_prime(nums):
    x = nums[177]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for p in primes:
        is_right_truncatable = True
        n = p
        while n > 0:
            if not is_prime(n):
                is_right_truncatable = False
                break
            n //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True