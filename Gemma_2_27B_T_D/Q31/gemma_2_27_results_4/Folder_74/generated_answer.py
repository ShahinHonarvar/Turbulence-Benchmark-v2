def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[48]):
        if nums[48] % i == 0:
            total += i
    return total == nums[48]