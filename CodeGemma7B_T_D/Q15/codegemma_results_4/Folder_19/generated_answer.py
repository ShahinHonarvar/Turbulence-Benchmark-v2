def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for num in nums[3:6]:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd if sum_odd else 0