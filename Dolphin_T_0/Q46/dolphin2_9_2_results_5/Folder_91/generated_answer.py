def gcf_three_nums(nums):
    a = nums[8]
    b = nums[9]
    c = nums[3]
    gcf = a
    while b != 0 and c != 0:
        gcf = (b if a % b == 0 else b, c)
        if gcf == c:
            break
        if gcf == b:
            a = b
        else:
            a = gcf
        b = gcf
    return gcf