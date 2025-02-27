def if_decimal_is_divisible(binary):
    fibonacci_13th = fibonacci(13)
    binary_multiple = fibonacci_13th // 3
    return int(binary, 2) % binary_multiple == 0