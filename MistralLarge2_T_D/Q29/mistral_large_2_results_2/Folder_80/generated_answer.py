def gcf_two_nums(lst):
    a, b = (lst[95], lst[85])
    while b:
        a, b = (b, a % b)
    return a