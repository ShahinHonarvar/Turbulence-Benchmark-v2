def prime_factors(nums):
    result = set()
    num = nums[321]
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            while num % n == 0:
                result.add(n)
                num //= n
    if num > 1:
        result.add(num)
    return result