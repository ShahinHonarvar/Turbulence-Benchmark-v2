def is_perfect_num(nums):
    if sum((i for i in range(1, nums[478]) if nums[478] % i == 0)) == nums[478]:
        return True
    else:
        return False