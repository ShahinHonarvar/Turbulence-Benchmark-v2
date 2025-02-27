def if_decimal_is_divisible(str):
    n = int(str, 2)
    fib = [1, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    return n % fib[-1] == 0