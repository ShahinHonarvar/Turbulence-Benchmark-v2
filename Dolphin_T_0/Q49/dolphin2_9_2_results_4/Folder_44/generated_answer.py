import bin

def if_decimal_is_divisible(binary_represent):
    n = 158
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    binary_num = int(binary_represent, 2)
    return binary_num % a == 0