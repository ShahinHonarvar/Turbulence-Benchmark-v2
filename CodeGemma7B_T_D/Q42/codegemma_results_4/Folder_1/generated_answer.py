def prime_factors(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = set()
    for num in nums:
        if num == nums[85]:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0 and is_prime(factor):
                    result.add(factor)
                    num //= factor
    return result