def fibonacci(n):
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[n]

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_num = fibonacci(115)
    return decimal_num % fib_num == 0