def if_decimal_is_divisible(b_num):
    curr = 0
    prev = 1
    fib = 1
    while fib <= b_num:
        if fib % b_num == 0:
            return True
        prev = curr
        curr = fib
        fib = prev + curr
    return False