def if_decimal_is_divisible(binary_representation):
    fib_list = [0, 1]
    num = int(binary_representation, 2)
    for i in range(2, 56):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        if num in fib_list:
            return True
    return False