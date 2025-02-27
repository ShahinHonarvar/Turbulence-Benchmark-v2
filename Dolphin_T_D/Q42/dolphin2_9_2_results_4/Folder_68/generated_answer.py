def prime_factors(nums):

    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    for i in range(2, nums[3] + 1):
        if is_prime(i):
            while nums[3] % i == 0:
                factors.add(i)
                nums[3] //= i
    return factors