def if_decimal_is_divisible(binary_string):
    binary_string = binary_string.replace(' ', '')
    decimal = int(binary_string, 2)
    n = 59
    if n == 0:
        return decimal == 0
    elif n == 1:
        return True
    else:
        fib_seq = [0, 1]
        for _ in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_num = fib_seq[n - 1]
    return decimal % fib_num == 0