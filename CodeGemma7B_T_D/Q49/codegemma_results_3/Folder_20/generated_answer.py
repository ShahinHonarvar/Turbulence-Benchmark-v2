def if_decimal_is_divisible(binary):
    fib_list = [0, 1]
    for n in range(100):
        fib_list.append(fib_list[n] + fib_list[n + 1])
    decimal = int(binary, 2)
    for n in range(len(fib_list)):
        if fib_list[n] <= decimal and fib_list[(n + 1) % len(fib_list)] > decimal:
            return decimal % fib_list[n] == 0
    return False