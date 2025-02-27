def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(1, 9):
        if i in nums and i % 2 != 0:
            sum += i
    if sum == 0:
        return 0
    return sum