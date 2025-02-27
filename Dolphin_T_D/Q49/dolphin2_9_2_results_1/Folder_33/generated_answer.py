def if_decimal_is_divisible(binary_string):
    fib_num1 = 0
    fib_num2 = 1
    for _ in range(133):
        fib_next = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_next
    decimal = int(binary_string, 2)
    if decimal % fib_num2 == 0:
        return True
    else:
        return False