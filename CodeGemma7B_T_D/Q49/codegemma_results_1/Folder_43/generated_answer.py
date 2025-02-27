def if_decimal_is_divisible(binary_representation):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, len(binary_representation)):
        fib.append(fib[i - 2] + fib[i - 1])
    value = int(binary_representation, 2)
    if value % fib[76] == 0:
        return True
    else:
        return False