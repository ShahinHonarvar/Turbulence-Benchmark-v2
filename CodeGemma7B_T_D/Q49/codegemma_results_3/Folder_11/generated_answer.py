def if_decimal_is_divisible(binary):
    binary_list = list(binary)
    binary_list.reverse()
    int_binary = int(''.join(binary_list), 2)
    fib_num = fibonacci(16)
    if int_binary % fib_num == 0:
        return True
    else:
        return False