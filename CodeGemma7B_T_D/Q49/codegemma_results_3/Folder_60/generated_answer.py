def if_decimal_is_divisible(binary_representation):
    generater = fibonacci_up_to(108)
    next_fib = next(generater)
    decimal = 0
    for digit in binary_representation:
        decimal = 2 * decimal + int(digit)
    return decimal % next_fib == 0

def fibonacci_up_to(num):
    first = 0
    second = 1
    while True:
        third = first + second
        if third > num:
            break
        yield third
        first, second = (second, third)