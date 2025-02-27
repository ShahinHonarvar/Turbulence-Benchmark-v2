def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, len(binary_str)):
        fib.append(fib[i - 1] + fib[i - 2])
    if int(binary_str, 2) % fib[int(binary_str, 2).bit_length() - 2] == 0:
        return True
    else:
        return False