def sum_odd_ints_inclusive(nums: list) -> int:
    sum = 0
    for i in range(30, 49):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum