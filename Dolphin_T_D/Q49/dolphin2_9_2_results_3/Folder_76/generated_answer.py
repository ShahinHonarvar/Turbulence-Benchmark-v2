def if_decimal_is_divisible(binary_number):
    fib_188 = [0, 1]
    for i in range(2, 188):
        fib_188.append(fib_188[i - 1] + fib_188[i - 2])
    mod = int(binary_number, 2) % fib_188[187]
    return mod == 0