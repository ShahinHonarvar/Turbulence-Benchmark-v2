def gcf_three_nums(nums):
    a = nums[9]
    b = nums[6]
    c = nums[2]
    gcf = a
    while b != 0 and c != 0:
        gcf = b if a > b else a
        gcf = c if gcf > c else c
        a = gcf
        b = a * (a // b)
        c = a * (a // c)
    return gcf