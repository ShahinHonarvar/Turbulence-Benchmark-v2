def if_decimal_is_divisible(binary):
    fib = [0]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib >= 1000000000:
            break
        fib.append(next_fib)
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    for num in fib[4:]:
        if num > decimal:
            break
        elif decimal % num == 0:
            return True
    return False