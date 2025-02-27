def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_177 = [0, 1]
    for i in range(2, 178):
        fib_177.append(fib_177[i - 1] + fib_177[i - 2])
    if decimal_number % fib_177[-1] == 0:
        return True
    else:
        return False