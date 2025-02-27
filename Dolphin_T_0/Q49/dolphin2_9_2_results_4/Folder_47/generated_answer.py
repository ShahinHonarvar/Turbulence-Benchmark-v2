def if_decimal_is_divisible(binary_string):

    def binary_to_decimal(binary_string):
        decimal_value = 0
        for i in range(len(binary_string)):
            decimal_value = decimal_value * 2 + int(binary_string[i])
        return decimal_value

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = binary_to_decimal(binary_string)
    fib_94 = fibonacci(94)
    if decimal_value % fib_94 == 0:
        return True
    else:
        return False