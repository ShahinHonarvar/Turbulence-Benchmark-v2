def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 2) + fibonacci(n - 1)

    def decimal(binary_string):
        result = 0
        for i in range(len(binary_string)):
            result += int(binary_string[i]) * 2 ** i
        return result
    return decimal(binary_string) % fibonacci(38) == 0