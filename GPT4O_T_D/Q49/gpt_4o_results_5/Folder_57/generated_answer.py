def if_decimal_is_divisible(binary_str):
    fibs = [0, 1]
    for _ in range(2, 81):
        fibs.append(fibs[-1] + fibs[-2])
    fib_80th = fibs[80]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_80th == 0