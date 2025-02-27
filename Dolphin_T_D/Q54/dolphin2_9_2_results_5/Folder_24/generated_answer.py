def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[65]
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = [n for n in primes if all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))]
    return sorted(right_truncatable_primes, reverse=True) or []