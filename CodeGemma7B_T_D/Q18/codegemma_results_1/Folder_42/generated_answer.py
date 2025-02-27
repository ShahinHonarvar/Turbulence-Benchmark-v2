def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    if len(nums) < 29 or len(nums) < 45:
        return 0
    if not all((isinstance(num, int) for num in nums)):
        return 0
    sum = 0
    for i in range(29, 46):
        if nums[i] % 27 == 0 or nums[i] % 81 == 0:
            sum += nums[i]
    return sum