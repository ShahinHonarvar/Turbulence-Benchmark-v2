def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(nums):

    def helper(n, primes):
        if n == 0:
            return primes
        if is_prime(n):
            primes.append(n)
        return helper(n // 10, primes)
    return sorted(helper(nums[33], []))