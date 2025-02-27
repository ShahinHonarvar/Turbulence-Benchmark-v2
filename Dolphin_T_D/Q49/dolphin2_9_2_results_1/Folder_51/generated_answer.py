def if_decimal_is_divisible(binary_string):
    num_fibonacci = 0
    a = 0
    b = 1
    while num_fibonacci < 16:
        a, b = (b, a + b)
        num_fibonacci += 1
    fib_17 = b
    num = int(binary_string, 2)
    return num % fib_17 == 0