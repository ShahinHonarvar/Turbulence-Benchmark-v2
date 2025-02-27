def if_decimal_is_divisible(binary_string):
    binary_to_decimal = int(binary_string, 2)
    i = 3
    num = 2
    fib = [0, 1]
    while True:
        if binary_to_decimal == num:
            if num % 134 == 0:
                return True
            else:
                return False
        fib.append(fib[i - 2] + fib[i - 1])
        i += 1
        num = fib[i - 1]