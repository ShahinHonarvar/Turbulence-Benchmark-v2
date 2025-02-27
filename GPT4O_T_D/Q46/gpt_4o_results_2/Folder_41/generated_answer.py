import math

def gcf_three_nums(numbers):

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    if len(numbers) < 95:
        return None
    a, b, c = (numbers[19], numbers[94], numbers[78])
    gcf_ab = gcf(a, b)
    return gcf(gcf_ab, c)