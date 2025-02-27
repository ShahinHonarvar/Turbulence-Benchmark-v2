def is_decimal_divisible_by_138_fib_num(binary_representation):
    decimal_num = 0
    factor = 2 ** (len(binary_representation) - 1)
    for digit in binary_representation:
        if digit == '1':
            decimal_num += factor
        factor //= 2
    fib_num = 1
    current_num = 1
    while True:
        if fib_num == 138:
            return decimal_num % fib_num == 0
        new_num = current_num + fib_num
        fib_num = current_num
        current_num = new_num