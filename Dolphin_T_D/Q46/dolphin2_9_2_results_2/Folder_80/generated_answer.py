def gcf(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcf(b, a % b)
    return gcf(a, b % a)

def gcf_three_nums(lst):
    return gcf(gcf(lst[13], lst[76]), lst[44])