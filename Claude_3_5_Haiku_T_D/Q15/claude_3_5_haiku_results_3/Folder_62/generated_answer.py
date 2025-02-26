def sum_odd_ints_inclusive(nums):
    if len(nums) <= 99:
        return 0
    total = 0
    for num in nums[91:100]:
        if num % 2 != 0:
            total += num
    return total