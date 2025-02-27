def gcf_three_nums(list_of_nums):
    a = list_of_nums[29]
    b = list_of_nums[74]
    c = list_of_nums[49]
    gcf = int(a)
    while a != b or b != c:
        if a < b:
            b = b - gcf
        elif b < a:
            a = a - gcf
        if b != c:
            if b < c:
                c = c - gcf
            elif c < b:
                b = b - gcf
    return gcf