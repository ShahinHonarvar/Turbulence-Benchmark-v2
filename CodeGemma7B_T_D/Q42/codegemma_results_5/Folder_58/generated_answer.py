def prime_factors(nums):
    factors = set()
    int_714_factors = set()
    for num in nums:
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num == 1:
            factors.add(num)
    if 714 in range(len(nums)):
        int_714_factors = factors.copy()
    return int_714_factors