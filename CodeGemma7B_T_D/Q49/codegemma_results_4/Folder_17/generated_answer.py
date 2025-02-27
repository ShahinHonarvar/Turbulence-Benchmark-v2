def if_decimal_is_divisible(binary_representation):
    fib_list = [0, 1]
    for i in range(2, 500):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % fib_list[153] == 0:
        return True
    else:
        return False