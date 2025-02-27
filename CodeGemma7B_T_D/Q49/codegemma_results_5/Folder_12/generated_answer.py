def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1]
    counter = 2
    while len(fib_list) < 66:
        fib_list.append(fib_list[counter - 1] + fib_list[counter - 2])
        counter += 1
    decimal_value = 0
    for i, digit in enumerate(binary_string):
        decimal_value += 2 ** i * int(digit)
    if decimal_value % fib_list[65] == 0:
        return True
    else:
        return False