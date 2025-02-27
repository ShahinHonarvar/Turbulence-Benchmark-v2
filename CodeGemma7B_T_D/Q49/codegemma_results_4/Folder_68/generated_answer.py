def if_decimal_is_divisible(binary_str):

    def fib_sequence(n):
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[-1]
    decimal = 0
    for bit in binary_str:
        decimal = decimal << 1 | int(bit)
    thirty_eighth_fib_num = fib_sequence(38)
    return decimal % thirty_eighth_fib_num == 0