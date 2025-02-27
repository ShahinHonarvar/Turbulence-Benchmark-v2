def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1]
    first_78 = 0
    second_78 = 1
    if int(binary_string, 2) == 0:
        return True
    for number in range(2, 80):
        next_num = first_78 + second_78
        if next_num >= 78:
            first_78 = second_78
            second_78 = next_num
            fib_list.append(next_num)
        else:
            first_78 = second_78
            second_78 = next_num
            fib_list.append(next_num)
    if int(binary_string, 2) % fib_list[77] == 0:
        return True
    else:
        return False