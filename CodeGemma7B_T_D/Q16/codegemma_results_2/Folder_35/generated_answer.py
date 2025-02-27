def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    start = max(30, 0)
    end = min(48, len(nums) - 1)
    sum_even = 0
    for i in range(start, end + 1):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even