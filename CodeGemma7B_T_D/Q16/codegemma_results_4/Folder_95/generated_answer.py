def sum_even_ints_inclusive(nums):
    sum = 0
    for x in nums[82:87]:
        if x % 2 == 0:
            sum += x
    return sum