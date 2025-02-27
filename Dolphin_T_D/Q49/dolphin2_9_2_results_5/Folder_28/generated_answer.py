def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fib = [0, 1]
    for i in range(2, 104):
        fib.append(fib[i - 1] + fib[i - 2])
    if n % fib[103] == 0:
        return True
    else:
        return False