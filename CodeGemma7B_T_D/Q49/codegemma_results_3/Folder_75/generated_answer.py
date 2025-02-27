def if_decimal_is_divisible(binary_str):
    memo = {}
    fib_idx = 189

    def fibonacci(n):
        if n in memo:
            return memo[n]
        if n in (0, 1):
            result = n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = result
        return result

    def to_decimal(binary_str):
        total_num = 0
        for ind, digit in enumerate(reversed(binary_str)):
            total_num += 2 ** ind * int(digit)
        return total_num
    if to_decimal(binary_str) % fibonacci(fib_idx) == 0:
        return True
    else:
        return False