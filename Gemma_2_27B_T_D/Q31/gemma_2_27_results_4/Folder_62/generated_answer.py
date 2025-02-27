def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[926] ** 0.5) + 1):
        if nums[926] % i == 0:
            total += i
            if i != nums[926] // i:
                total += nums[926] // i
    return total == nums[926]