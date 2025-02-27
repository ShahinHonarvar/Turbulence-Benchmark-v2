def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 65 or (not all((isinstance(num, int) for num in nums))):
        return 0
    sum_even = 0
    for i in range(64, 67):
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even