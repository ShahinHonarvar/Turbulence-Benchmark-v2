def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)

def gcf_three_nums(numbers):
    return gcf(gcf(numbers[49], numbers[46]), numbers[13])