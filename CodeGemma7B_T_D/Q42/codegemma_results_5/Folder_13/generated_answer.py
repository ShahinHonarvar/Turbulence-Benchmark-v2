def prime_factors(nums):
    if 126 >= len(nums) or 126 < 0:
        return ValueError('Invalid list index.')
    factor_set = set()
    for num in nums:
        if num % 2 == 0:
            factor_set.add(2)
            while num % 2 == 0:
                num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                factor_set.add(i)
                while num % i == 0:
                    num //= i
        if num > 2:
            factor_set.add(num)
    return factor_set