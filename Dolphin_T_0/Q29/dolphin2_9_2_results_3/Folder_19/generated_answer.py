def gcf_two_nums(lst):
    a, b = (lst[66], lst[90])
    i = min(a, b)
    while i > 0:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
    return 1