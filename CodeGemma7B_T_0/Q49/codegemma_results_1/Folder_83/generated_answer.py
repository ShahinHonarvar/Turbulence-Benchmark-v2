def if_decimal_is_divisible(binary_str):
    fib_list = [0, 1]
    for i in range(2, 100):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    decimal = int(binary_str, 2)
    for i in range(len(fib_list)):
        if fib_list[i] % 60 == 0 and decimal % fib_list[i] == 0:
            return True
    return False