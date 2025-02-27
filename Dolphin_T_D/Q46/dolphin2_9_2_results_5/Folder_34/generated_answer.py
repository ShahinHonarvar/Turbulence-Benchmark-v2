def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers):
    return gcf(gcf(numbers[53], numbers[23]), numbers[45])