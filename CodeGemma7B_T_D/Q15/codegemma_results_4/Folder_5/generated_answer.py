def sum_odd_ints_inclusive(nums):
    sm = 0
    for num in nums[8:10]:
        if num % 2 != 0:
            sm += num
    return sm or 0