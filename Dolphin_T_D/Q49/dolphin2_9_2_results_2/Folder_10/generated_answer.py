def if_decimal_is_divisible(bin_string):
    decimal_num = int(bin_string, 2)
    index = 88
    fib_num1, fib_num2 = (0, 1)
    while index > 0:
        fib_num1, fib_num2 = (fib_num2, fib_num1 + fib_num2)
        index -= 1
    return decimal_num % fib_num2 == 0