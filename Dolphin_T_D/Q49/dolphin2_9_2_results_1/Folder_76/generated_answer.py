def if_decimal_is_divisible(s):
    fib_188 = [0, 1]
    for i in range(2, 188):
        fib_188.append(fib_188[i - 2] + fib_188[i - 1])
    decimal = int(s, 2)
    if decimal % fib_188[-1] == 0:
        return True
    else:
        return False