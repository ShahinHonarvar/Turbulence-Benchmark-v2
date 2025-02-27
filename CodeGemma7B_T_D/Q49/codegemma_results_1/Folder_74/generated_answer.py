def if_decimal_is_divisible(binary_str):

    def fibonacci(number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)

    def binary_to_decimal(binary_str):
        decimal = 0
        for digit in binary_str:
            decimal = decimal * 2 + int(digit)
        return decimal
    fib_index = 2
    fib_value = fibonacci(fib_index)
    while fib_value < 166:
        fib_index += 1
        fib_value = fibonacci(fib_index)
    if fibonacci(fib_index) % binary_to_decimal(binary_str) == 0:
        return True
    else:
        return False