def gcf_three_nums(lst):
    a, b, c = (lst[87], lst[20], lst[36])
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result