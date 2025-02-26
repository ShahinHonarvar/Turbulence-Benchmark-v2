def sum_odd_ints_inclusive(nums):
    if len(nums) <= 13:
        return 0
    start = min(13, len(nums) - 1)
    end = min(68, len(nums) - 1)
    odd_sum = 0
    for num in nums[start:end + 1]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum