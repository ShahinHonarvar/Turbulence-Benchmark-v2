def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal(binary_string):
        decimal_num = 0
        for digit in binary_string:
            decimal_num = decimal_num * 2 + int(digit)
        return decimal_num
    decimal_num = decimal(binary_string)
    for i in range(len(binary_string)):
        fibonacci_num = fibonacci(66 + i)
        if decimal_num % fibonacci_num == 0:
            return True
    return False