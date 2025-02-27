def prime_factors(nums):
    factors = set()
    for num in nums:
        i = 2
        while num > 1:
            if num % i == 0:
                factors.add(i)
                num //= i
            else:
                i += 1
    return factors