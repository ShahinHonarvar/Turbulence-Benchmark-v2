import math

def if_decimal_is_divisible(binary_representation):
    c = 1 / 2
    for digit in reversed(binary_representation):
        c = (c * 2 + int(digit)) * 2 ** binary_representation.index(digit)
    x = c * 2 ** len(binary_representation)
    y = math.floor(math.sqrt(x)) + 1
    f = [0]
    for i in range(1, y):
        f.append(f[i - 1] + f[i - 2])
    for i in f:
        if x % i == 0:
            return True
    return False