def if_decimal_is_divisible(bin_string):
    bin_list = list(bin_string.strip())
    decimal = 0
    for i in range(len(bin_list)):
        decimal += int(bin_list[-(i + 1)]) * 2 ** i
    fib_list = [0, 1]
    while len(fib_list) < 29:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if decimal % fib_list[28] == 0:
        return True
    return False