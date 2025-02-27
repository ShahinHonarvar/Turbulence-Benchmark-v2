def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    a, b = (0, 1)
    while a < 139:
        a, b = (b, a + b)
        fibonacci_seq.append(a)
    return decimal % fibonacci_seq[-1] == 0