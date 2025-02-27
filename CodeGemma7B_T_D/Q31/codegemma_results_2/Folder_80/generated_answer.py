def if_perfect_num(nums):
    if nums[746] % sum([i for i in range(1, nums[746]) if nums[746] % i == 0]) == 0:
        return True
    return False