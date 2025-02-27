def if_decimal_is_divisible(binary_representation):
    binary_list = list(binary_representation)
    binary_int = 0
    for digit in binary_list:
        binary_int = (binary_int << 1) + int(digit)
    counter = 0
    fib_current = 0
    fib_next = 1
    while counter < 180:
        fib_current, fib_next = (fib_next, fib_current + fib_next)
        counter += 1
    return binary_int % fib_current == 0