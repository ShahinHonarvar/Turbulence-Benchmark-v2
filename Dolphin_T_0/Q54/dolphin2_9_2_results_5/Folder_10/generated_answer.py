def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(nums):
    x = nums[38]
    primes = [str(n) for n in range(1, x) if is_prime(n)]
    right_truncatable_primes = []
    for prime in primes:
        if all([is_prime(int(prime[i:])) for i in range(len(prime) - 1)]):
            right_truncatable_primes.append(int(prime))
    return sorted(right_truncatable_primes, reverse=True)