def if_decimal_is_divisible(binary_num):
    index_fib = 114
    fib = [0, 1]
    for i in range(2, index_fib + 1):
        fib.append(fib[-2] + fib[-1])
    num = int(binary_num, 2)
    return num % fib[index_fib] == 0