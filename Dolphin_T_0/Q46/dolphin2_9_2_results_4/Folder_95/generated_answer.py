def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def gcf_three_nums(lst):
    return gcf(lst[87], gcf(lst[20], lst[36]))