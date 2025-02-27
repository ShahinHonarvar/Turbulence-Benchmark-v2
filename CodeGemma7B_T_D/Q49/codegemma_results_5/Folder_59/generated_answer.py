def if_decimal_is_divisible(binary_representation):
    fib_list = [0, 1]
    num = int(binary_representation, 2)
    length = len(binary_representation)
    index = 2
    for i in range(length):
        fib_list.append(fib_list[i] + fib_list[i + 1])
        if fib_list[index] >= num:
            if num % fib_list[index] == 0:
                return True
            else:
                index -= 1
                continue
        index += 1
    return False