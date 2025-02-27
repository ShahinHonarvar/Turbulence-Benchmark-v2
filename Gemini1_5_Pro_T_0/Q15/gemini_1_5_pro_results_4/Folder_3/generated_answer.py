def sum_odd_ints_inclusive(nums: list) -> int:
    sum = 0
    for i in range(max(0, min(62, len(nums))), min(93, len(nums))):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum