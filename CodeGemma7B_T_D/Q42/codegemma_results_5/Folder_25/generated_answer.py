def prime_factors(nums):
    for number in nums:
        if number == nums[90]:
            factor = 2
            factors = set()
            while factor * factor <= number:
                if number % factor == 0:
                    factors.add(factor)
                    number //= factor
                else:
                    factor += 1
            if number > 1:
                factors.add(number)
            return factors