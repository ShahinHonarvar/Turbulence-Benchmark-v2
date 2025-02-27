def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        decimal = 0
        for i in range(len(binary_str)):
            decimal = decimal * 2 + int(binary_str[i])
        return decimal

    def nth_fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    decimal = binary_to_decimal(binary_str)
    fibonacci_99 = nth_fibonacci(99)
    return decimal % fibonacci_99 == 0