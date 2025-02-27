def if_decimal_is_divisible(b):
    decimal_value = int(b, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 68):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    fib_67 = fibonacci_numbers[67]
    return decimal_value % fib_67 == 0