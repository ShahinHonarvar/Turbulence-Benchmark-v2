def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for num in nums[4:5]:
        if num % 2 != 0:
            sum_odd += num
    if sum_odd == 0:
        return 0
    else:
        return sum_odd