def if_perfect_num(nums):
    if nums[54] == sum([i for i in range(1, nums[54]) if nums[54] % i == 0]):
        return True
    return False