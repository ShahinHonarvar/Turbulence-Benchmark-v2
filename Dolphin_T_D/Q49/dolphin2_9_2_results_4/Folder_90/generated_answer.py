def if_decimal_is_divisible(binary_str):
    dec = 0
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            dec += 2 ** (len(binary_str) - 1 - i)
    fib = [0, 1]
    i = 2
    while i < 177:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    if dec % fib[-1] == 0:
        return True
    else:
        return False