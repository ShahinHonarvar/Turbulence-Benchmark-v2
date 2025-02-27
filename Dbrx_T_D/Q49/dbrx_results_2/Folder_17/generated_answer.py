def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(153) + 1
    if fibonacci_number > decimal_number:
        return False
    while fibonacci_number <= decimal_number:
        if decimal_number % fibonacci_number == 0:
            return True
        fibonacci_number = fibonacci(fibonacci_number)
    return False

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)