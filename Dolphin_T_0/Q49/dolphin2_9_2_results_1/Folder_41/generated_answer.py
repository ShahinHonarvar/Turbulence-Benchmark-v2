def if_decimal_is_divisible(binary):
    n = 0
    for i in range(len(binary)):
        n += int(binary[i]) * 2 ** (len(binary) - 1 - i)
    m = 0
    fib = [0, 1]
    while len(fib) <= 67:
        fib.append(fib[-1] + fib[-2])
    k = fib[66]
    if n % k == 0:
        return True
    else:
        return False