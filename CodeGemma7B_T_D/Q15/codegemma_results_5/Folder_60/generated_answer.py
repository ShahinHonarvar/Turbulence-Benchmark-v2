def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for num in nums[75:86]:
        if num % 2 != 0:
            sum_odd += num
    if sum_odd == 0:
        return 0
    return sum_odd