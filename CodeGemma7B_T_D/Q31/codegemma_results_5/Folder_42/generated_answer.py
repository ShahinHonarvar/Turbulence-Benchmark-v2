def if_perfect_num(nums):
    if nums[276] % sum([i for i in range(1, nums[276]) if nums[276] % i == 0]) == 0:
        return True
    return False