def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_127 = 144754627925807269538520153832432599
    return decimal % fib_127 == 0