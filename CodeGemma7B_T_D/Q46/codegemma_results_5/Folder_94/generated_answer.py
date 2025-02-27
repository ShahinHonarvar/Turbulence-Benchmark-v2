def gcf_three_nums(lst):
    a, b, c = (lst[56], lst[88], lst[51])
    common_factor = a
    for num in (b, c):
        while num % common_factor != 0:
            common_factor -= 1
    return common_factor