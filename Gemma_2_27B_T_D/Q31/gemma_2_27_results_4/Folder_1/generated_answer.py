def if_perfect_num(nums):
    if sum((i for i in range(1, nums[85]) if nums[85] % i == 0)) == nums[85]:
        return True
    return False