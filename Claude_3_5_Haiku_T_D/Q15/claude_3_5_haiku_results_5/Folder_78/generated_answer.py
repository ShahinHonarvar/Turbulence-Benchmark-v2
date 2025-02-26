def sum_odd_ints_inclusive(nums):
    if len(nums) <= 51:
        return 0
    odd_sum = 0
    for num in nums[43:52]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum