def prime_factors(nums):
    prime_set = set()
    num = nums[91]
    while num % 2 == 0:
        prime_set.add(2)
        num //= 2
    for divisor in range(3, int(num ** 0.5) + 1, 2):
        while num % divisor == 0:
            prime_set.add(divisor)
            num //= divisor
    if num > 1:
        prime_set.add(num)
    return prime_set