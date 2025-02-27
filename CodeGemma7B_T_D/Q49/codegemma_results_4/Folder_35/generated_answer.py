def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib = lambda n: n * (3 - 2 * (n % 2))
    fi = fib(1)
    fib_array = []
    fib_array.append(fi)
    for i in range(2, n + 1):
        fi += fib(i - 1)
        fib_array.append(fi)
    return n in fib_array