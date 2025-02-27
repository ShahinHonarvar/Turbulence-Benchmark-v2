def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def fibonacci_nums(n):
    for i, num in enumerate(fibonacci()):
        if i == n:
            return num

def decode_binary_string(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_representation):
    decimal_num = decode_binary_string(binary_representation)
    fib_num = fibonacci_nums(114)
    return decimal_num % fib_num == 0