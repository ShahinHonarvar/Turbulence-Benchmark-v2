def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[73]):
        if nums[73] % i == 0:
            total += i
    return total == nums[73]