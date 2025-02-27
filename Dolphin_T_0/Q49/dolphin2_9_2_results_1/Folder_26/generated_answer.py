def if_decimal_is_divisible(binary_string):
    n = 0
    for c in binary_string:
        n = n * 2 + int(c)
    fib = [0, 1]
    while len(fib) < 139:
        fib.append(fib[-1] + fib[-2])
    fib_138 = fib[-1]
    return n % fib_138 == 0