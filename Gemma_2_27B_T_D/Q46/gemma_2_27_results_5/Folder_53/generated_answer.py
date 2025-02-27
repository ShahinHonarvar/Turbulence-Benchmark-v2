def gcf_three_nums(nums):
    a = nums[66]
    b = nums[56]
    c = nums[92]
    while True:
        if a == b == c:
            return a
        if a < b:
            b -= a
        elif b < c:
            c -= b
        else:
            a -= b