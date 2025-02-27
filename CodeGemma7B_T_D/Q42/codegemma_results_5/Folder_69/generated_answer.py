def prime_factors(nums):
    prime_set = set()
    num = nums[459]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_set.add(i)
            num //= i
    return prime_set