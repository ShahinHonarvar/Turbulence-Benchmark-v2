def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    for _ in range(64):
        fib.append(fib[-1] + fib[-2])
    fib_66th = fib[66]
    decimal_value = int(binary_representation, 2)
    return decimal_value % fib_66th == 0