def sum_even_ints_inclusive(nums: list) -> int:
    sum = 0
    for i in range(111, 112):
        if i < len(nums) and nums[i] % 2 == 0:
            sum += nums[i]
    return sum