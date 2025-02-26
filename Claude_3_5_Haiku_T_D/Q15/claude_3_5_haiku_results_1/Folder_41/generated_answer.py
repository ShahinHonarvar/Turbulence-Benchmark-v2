def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) <= 6:
        return 0
    odd_sum = 0
    for num in nums[6:7]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum