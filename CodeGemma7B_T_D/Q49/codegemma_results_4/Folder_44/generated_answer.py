def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)

    def fibonacci(index):
        if index < 2:
            return index
        else:
            return fibonacci(index - 1) + fibonacci(index - 2)
    fibonacci_index = 159
    fibonacci_value = fibonacci(fibonacci_index)
    return decimal_int % fibonacci_value == 0