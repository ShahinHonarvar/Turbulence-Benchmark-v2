def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcf(lst[44], gcf(lst[91], lst[42]))