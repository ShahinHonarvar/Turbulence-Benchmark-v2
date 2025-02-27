def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[97]):
        if nums[97] % i == 0:
            total += i
    return total == nums[97]