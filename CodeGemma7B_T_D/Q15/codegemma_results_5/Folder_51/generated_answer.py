def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(1, 9):
        if i in nums and i % 2 != 0:
            sum_odd += i
    return sum_odd if sum_odd else 0