def if_decimal_is_divisible(binary_representation):
    fib_dict = {0: 0, 1: 1}
    fib_num = 1
    for index in range(2, 128):
        fib_num = fib_dict[index - 1] + fib_dict[index - 2]
        fib_dict[index] = fib_num
    sum_of_digits = 0
    for digit in binary_representation:
        sum_of_digits += int(digit)
    return sum_of_digits % fib_dict[127] == 0