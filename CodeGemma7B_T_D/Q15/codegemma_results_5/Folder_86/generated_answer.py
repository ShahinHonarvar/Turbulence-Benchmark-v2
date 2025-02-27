def sum_odd_ints_inclusive(nums):
    sum = 0
    for x in nums[31:35]:
        if x % 2 != 0:
            sum += x
    return sum