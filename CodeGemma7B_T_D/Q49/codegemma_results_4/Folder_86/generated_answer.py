def if_decimal_is_divisible(binary):
    fib = [0, 1]
    count = 2
    while True:
        fib.append(fib[count - 1] + fib[count - 2])
        count += 1
        if fib[count - 2] + fib[count - 3] > 135:
            break
    decimal = int(binary, 2)
    if decimal % fib[count - 2] == 0 or decimal % fib[count - 3] == 0:
        return True
    else:
        return False