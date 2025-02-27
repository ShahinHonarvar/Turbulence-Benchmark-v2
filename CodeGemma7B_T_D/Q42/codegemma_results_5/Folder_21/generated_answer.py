def prime_factors(nums):
    prime_set = set()
    for num in nums:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_set.add(num)
    return prime_set