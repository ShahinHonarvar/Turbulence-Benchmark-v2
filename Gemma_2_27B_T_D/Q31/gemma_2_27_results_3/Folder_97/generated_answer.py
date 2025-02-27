def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[132]):
        if nums[132] % i == 0:
            total += i
    if total == nums[132]:
        return True
    else:
        return False