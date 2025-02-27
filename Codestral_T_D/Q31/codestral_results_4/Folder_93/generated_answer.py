def if_perfect_num(nums):
    if sum((i for i in range(1, nums[45]) if nums[45] % i == 0)) == nums[45]:
        return True
    else:
        return False