def prime_factors(nums):
    prime_factors_set = set()
    num = nums[132]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_factors_set.add(i)
            while num % i == 0:
                num = num // i
    if num > 1:
        prime_factors_set.add(num)
    return prime_factors_set