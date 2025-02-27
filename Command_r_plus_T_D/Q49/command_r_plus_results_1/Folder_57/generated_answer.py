def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_80th_num = 0
    a, b = (0, 1)
    for _ in range(80):
        a, b = (b, a + b)
    for char in binary_str:
        if char not in ['0', '1']:
            raise ValueError('Input must be a binary string.')
    decimal_num = int(binary_str, 2)
    return decimal_num % a == 0