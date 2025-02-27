import math

def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return True
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return True
        return False
    return set((n for n in numbers[74:96] if is_composite(n)))