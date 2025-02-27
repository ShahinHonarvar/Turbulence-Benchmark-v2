def if_decimal_is_divisible(binary_str):

    def get_next_fib(fib_list):
        return fib_list[-1] + fib_list[-2]
    fib_list = [0, 1]
    fib_index = 0
    while True:
        fib_list.append(get_next_fib(fib_list))
        fib_index += 1
        if fib_list[fib_index] > 199:
            break
    fib_to_check = fib_list[fib_index - 1]
    decimal_to_check = int(binary_str, 2)
    if decimal_to_check % fib_to_check == 0:
        return True
    else:
        return False