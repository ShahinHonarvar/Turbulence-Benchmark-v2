def if_decimal_is_divisible(binary_rep):
    num = int(binary_rep, 2)
    fib_index = 137
    fib_a, fib_b = (0, 1)
    for _ in range(fib_index):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    if num % fib_b == 0:
        return True
    else:
        return False