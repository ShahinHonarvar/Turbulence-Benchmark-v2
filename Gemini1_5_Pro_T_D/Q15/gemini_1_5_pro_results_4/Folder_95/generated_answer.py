def sum_odd_ints_inclusive(nums: list[int]) -> int:
    sum = 0
    for i in range(82, 87):
        if i < len(nums) and nums[i] % 2 != 0:
            sum += nums[i]
    return sum