def sum_odd_ints_inclusive(nums):
    if len(nums) < 5:
        return 0
    total = 0
    for num in nums[4:5]:
        if num % 2 != 0:
            total += num
    return total