def if_perfect_num(nums):
    if nums[92] == sum((i for i in range(1, nums[92]) if nums[92] % i == 0)):
        return True
    return False