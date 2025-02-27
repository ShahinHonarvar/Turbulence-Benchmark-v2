def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[93]):
        if nums[93] % i == 0:
            total += i
    return total == nums[93]