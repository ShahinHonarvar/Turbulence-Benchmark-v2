def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibonacci_number = 0
    fibonacci_1 = 0
    fibonacci_2 = 1
    for i in range(1, 87):
        fibonacci_number = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = fibonacci_number
    if n % fibonacci_number == 0:
        return True
    else:
        return False