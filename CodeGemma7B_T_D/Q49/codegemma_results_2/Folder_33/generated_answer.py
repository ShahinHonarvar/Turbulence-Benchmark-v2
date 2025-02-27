def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fib = [0] * (num + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, num + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    for i in range(num + 1):
        if fib[i] >= num:
            if num % fib[i] == 0:
                return True
            break
    return False