def if_decimal_is_divisible(binary='111110001'):

    def is_divisible(fib_index):
        fib_list = [0, 1]
        for x in range(fib_index):
            fib_list.append(fib_list[x] + fib_list[x + 1])
        return fib_list[fib_index] % int(binary, 2) == 0
    index = 159
    while not is_divisible(index):
        index += 1
    return is_divisible(index)