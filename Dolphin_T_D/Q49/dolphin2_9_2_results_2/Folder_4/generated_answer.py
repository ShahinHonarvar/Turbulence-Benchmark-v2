def if_decimal_is_divisible(bin_number):
    num = int(bin_number, 2)
    i = 0
    fib1 = 0
    fib2 = 0
    fib3 = 1
    while i < 118:
        fib2 = fib3
        fib3 = fib2 + fib1
        fib1 = fib2
        i += 1
    if num % fib3 == 0:
        return True
    else:
        return False