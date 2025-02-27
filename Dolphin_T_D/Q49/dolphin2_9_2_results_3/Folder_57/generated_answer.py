def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib = [0, 1]
    for i in range(2, 80):
        fib.append(fib[i - 1] + fib[i - 2])
    if decimal % fib[79] == 0:
        return True
    else:
        return False