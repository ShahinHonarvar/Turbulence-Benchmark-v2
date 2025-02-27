def if_perfect_num(nums):
    if nums[45] == sum((i for i in range(2, nums[45]) if nums[45] % i == 0)) + nums[45]:
        return True
    return False