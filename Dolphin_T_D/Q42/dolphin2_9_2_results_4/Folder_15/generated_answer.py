def prime_factors(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    factors = set()
    num = nums[10]
    for i in range(2, num):
        if is_prime(i) and num % i == 0:
            factors.add(i)
    return factors