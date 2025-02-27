def if_decimal_is_divisible(binary_str):
    fib_num = 0
    first_multiple_of_135_fib_num = 864
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            fib_num = fib_num + pow(2, len(binary_str) - i - 1)
    return fib_num % first_multiple_of_135_fib_num == 0