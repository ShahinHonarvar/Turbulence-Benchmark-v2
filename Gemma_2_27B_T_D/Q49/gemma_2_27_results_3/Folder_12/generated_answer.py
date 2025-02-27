def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_66 = 578063794386508073961449862253041184444169190391
    return decimal_num % fib_66 == 0