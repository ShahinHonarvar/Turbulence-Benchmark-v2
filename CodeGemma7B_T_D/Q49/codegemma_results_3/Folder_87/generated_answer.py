def if_decimal_is_divisible(binary_representation):
    fib_num_180 = fibonacci_180()
    decimal_value = int(binary_representation, 2)
    if decimal_value % fib_num_180 == 0:
        return True
    else:
        return False

def fibonacci_180():
    fib_numbers = []
    a, b = (0, 1)
    for _ in range(180):
        fib_numbers.append(a)
        a, b = (b, a + b)
    return fib_numbers[179]