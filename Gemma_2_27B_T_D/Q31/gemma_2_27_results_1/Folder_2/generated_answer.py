def if_perfect_num(nums):
    if sum([i for i in range(1, nums[702]) if nums[702] % i == 0]) == nums[702]:
        return True
    return False