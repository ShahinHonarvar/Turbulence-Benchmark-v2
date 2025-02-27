def if_decimal_is_divisible(binary_str):
    binary_num = int(binary_str, 2)
    fibonacci_num_160 = fibonacci(160)
    return binary_num % fibonacci_num_160 == 0

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)