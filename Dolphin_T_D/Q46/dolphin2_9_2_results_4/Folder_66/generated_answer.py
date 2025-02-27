def gcf_three_nums(lst):
    a, b, c = (lst[92], lst[69], lst[95])
    i = min(a, b, c)
    while i >= 1:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
        i -= 1
    return 1