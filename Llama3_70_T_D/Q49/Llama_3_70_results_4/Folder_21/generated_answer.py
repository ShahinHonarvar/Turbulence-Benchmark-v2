def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    num = int(binary_str, 2)
    return num % fibonacci(195) == 0