def if_perfect_num(nums):
    if sum([i for i in range(1, nums[926]) if nums[926] % i == 0]) == nums[926]:
        return True
    return False