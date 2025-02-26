def if_decimal_is_divisible(binary_str):

    def fibonacci_80th():
        if_prev, if_curr = (0, 1)
        for _ in range(78):
            if_prev, if_curr = (if_curr, if_prev + if_curr)
        return if_curr

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_80 = fibonacci_80th()
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_80 == 0