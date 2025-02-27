def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = nums[35]
    factors = []
    i = 2
    while i <= target:
        if target % i == 0 and is_prime(i):
            factors.append(i)
            target = target / i
        else:
            i += 1
    return set(factors)