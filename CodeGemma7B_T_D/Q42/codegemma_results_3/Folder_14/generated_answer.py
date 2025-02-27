def prime_factors(nums):
    prime_factor = set()
    num = nums[17]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            prime_factor.add(i)
            num //= i
    if num != 1:
        prime_factor.add(num)
    return prime_factor