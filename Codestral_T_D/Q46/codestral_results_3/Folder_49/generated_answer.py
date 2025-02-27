def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcf(gcf(lst[34], lst[38]), lst[77])