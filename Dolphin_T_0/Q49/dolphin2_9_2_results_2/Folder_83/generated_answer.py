def if_decimal_is_divisible(binary_representation):
    n = 60
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    fib = fib[n]
    decimal = int(binary_representation, 2)
    if decimal % fib == 0:
        return True
    else:
        return False