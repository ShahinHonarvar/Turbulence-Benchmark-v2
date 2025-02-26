def if_decimal_is_divisible(binary_str):

    def fibonacci_sixth_number():
        fib = [0, 1, 1, 2, 3, 5]
        return fib[5]
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_sixth_number() == 0