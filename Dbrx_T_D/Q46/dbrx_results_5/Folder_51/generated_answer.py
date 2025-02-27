import math

def gcf_three_nums(numbers):

    def gcf(a, b):
        return math.gcd(a, b) if b != 0 else a
    gcf_ab = gcf(numbers[21], numbers[69])
    gcf_result = gcf(gcf_ab, numbers[41])
    return gcf_result