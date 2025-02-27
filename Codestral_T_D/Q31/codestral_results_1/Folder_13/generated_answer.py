def if_perfect_num(nums):
    if sum((i for i in range(1, nums[126]) if nums[126] % i == 0)) == nums[126]:
        return True
    return False