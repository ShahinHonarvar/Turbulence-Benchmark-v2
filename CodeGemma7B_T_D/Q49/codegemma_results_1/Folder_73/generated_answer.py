def if_decimal_is_divisible(binary_str):
    fib, num = ([0, 1], 2)
    bin_to_dec = 0
    for digit in binary_str:
        bin_to_dec = bin_to_dec * 2 + int(digit)
    while num < 1013:
        fib.append(fib[num - 1] + fib[num - 2])
        num += 1
    if bin_to_dec % fib[1000] == 0:
        return True
    else:
        return False