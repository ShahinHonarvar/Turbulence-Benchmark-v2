import math

def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(lst[307], lst[920]), lst[463])