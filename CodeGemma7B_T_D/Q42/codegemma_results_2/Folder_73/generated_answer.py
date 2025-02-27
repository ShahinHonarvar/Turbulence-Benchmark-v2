def prime_factors(nums):
    factors = set()
    for num in nums:
        i = 2
        while i * i <= num:
            if num % i == 0:
                factors.add(i)
                num //= i
            else:
                i += 1
        if num > 1:
            factors.add(num)
    if 41 < len(nums) <= 41:
        return factors