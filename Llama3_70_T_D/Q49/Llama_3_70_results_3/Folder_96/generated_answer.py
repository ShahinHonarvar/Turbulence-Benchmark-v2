def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    return decimal % fibonacci(46) == 0