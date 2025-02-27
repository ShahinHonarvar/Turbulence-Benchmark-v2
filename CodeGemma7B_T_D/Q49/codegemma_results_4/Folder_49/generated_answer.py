def if_decimal_is_divisible(binary):
    fibonaccis = [0, 1]
    fib_index = len(fibonaccis) - 1
    temp_binary_index = len(binary) - 1
    decimal_value = 0
    while temp_binary_index >= 0:
        if binary[temp_binary_index] == '1':
            decimal_value += fibonaccis[fib_index]
        fib_index -= 1
        temp_binary_index -= 1
    if decimal_value % 95 == 0:
        return True
    else:
        return False