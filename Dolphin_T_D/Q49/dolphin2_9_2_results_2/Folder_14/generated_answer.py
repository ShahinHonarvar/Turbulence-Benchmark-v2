def if_decimal_is_divisible(binary):
    fib_27 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393]
    dec_num = int(binary, 2)
    return dec_num % fib_27[26] == 0