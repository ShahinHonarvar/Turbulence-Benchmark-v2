def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        n1, n2 = (0, 1)
        for _ in range(2, n + 1):
            n1, n2 = (n2, n1 + n2)
        return n2

def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_num = fibonacci(187)
    return decimal % fib_num == 0