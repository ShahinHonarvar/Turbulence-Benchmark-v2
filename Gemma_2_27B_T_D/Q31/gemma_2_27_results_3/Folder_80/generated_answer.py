def if_perfect_num(nums):
    if sum((i for i in range(1, nums[746]) if nums[746] % i == 0)) == nums[746]:
        return True
    return False