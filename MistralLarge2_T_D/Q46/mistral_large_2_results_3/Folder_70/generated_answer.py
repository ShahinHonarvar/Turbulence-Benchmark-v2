def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcf(gcf(lst[990], lst[671]), lst[711])