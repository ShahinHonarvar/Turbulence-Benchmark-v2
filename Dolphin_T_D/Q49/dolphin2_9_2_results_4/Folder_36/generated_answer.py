def if_decimal_is_divisible(binary_string):
    binary_string = binary_string.replace(' ', '')
    decimal_number = int(binary_string, 2)
    fib_num = [0, 1]
    while len(fib_num) <= 150:
        fib_num.append(fib_num[-1] + fib_num[-2])
    fib_num = fib_num[150]
    if decimal_number % fib_num == 0:
        return True
    return False