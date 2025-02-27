def if_decimal_is_divisible(binary_num):
    num = int(binary_num, 2)
    fib = [0, 1]
    for i in range(2, num + 1):
        fib.append(fib[-1] + fib[-2])
    if num in fib:
        return True
    else:
        return False