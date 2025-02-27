def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(55, 99, 2):
        try:
            num = nums[i]
            if num % 2 != 0:
                sum_odd += num
        except IndexError:
            pass
    return sum_odd