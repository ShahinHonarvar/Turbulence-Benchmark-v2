def if_decimal_is_divisible(binary_string):
    binary_length = len(binary_string)
    decimal = 0
    for i in range(binary_length):
        decimal += int(binary_string[i]) * 2 ** (binary_length - i - 1)
    fib_num = 0
    fib_index = 0
    while decimal > fib_num:
        fib_num = fib_index + fib_num
        fib_index += 1
    if fib_num % 13 == 0 and fib_index % 2 == 0:
        return True
    else:
        return False