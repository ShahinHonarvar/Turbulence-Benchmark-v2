def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    decimal_number = 0
    for digit in binary_representation:
        decimal_number = (decimal_number << 1) + int(digit)
    for i in range(32):
        if fibonacci(i + 1) == decimal_number + 16:
            return True
    return False