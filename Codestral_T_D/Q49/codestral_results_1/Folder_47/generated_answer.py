def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_list = [0, 1]
    while len(fib_list) < 95:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return decimal_number % fib_list[94] == 0