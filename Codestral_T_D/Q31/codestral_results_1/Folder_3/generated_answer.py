def if_perfect_num(nums):
    if nums[100] < 1:
        return False
    div_sum = sum([i for i in range(1, nums[100]) if nums[100] % i == 0])
    return div_sum == nums[100]