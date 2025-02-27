def if_decimal_is_divisible(binary_string):

    def binary_to_decimal(binary_string):
        decimal = 0
        for i in range(len(binary_string)):
            decimal = decimal * 2 + int(binary_string[i])
        return decimal
    n = 9
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal_value = binary_to_decimal(binary_string)
    return decimal_value % fib[n] == 0