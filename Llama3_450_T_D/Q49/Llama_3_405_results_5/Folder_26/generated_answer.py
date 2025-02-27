def if_decimal_is_divisible(binary_string):

    def fibonacci(n, memo={}):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n not in memo:
            memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]
    decimal = int(binary_string, 2)
    return decimal % fibonacci(137) == 0