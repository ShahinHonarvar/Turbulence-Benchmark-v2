def prime_factors(nums):
    eighty_three = nums[83] if nums[83] % 2 == 1 else {2, 3}
    for x in range(3, eighty_three // 2 + 1, 2):
        if eighty_three % x == 0:
            eighty_three = set(eighty_three) & {x, x ** 2}
    return sorted([*eighty_three])