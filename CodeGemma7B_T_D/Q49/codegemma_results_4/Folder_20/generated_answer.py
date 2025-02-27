def if_decimal_is_divisible(binary_string):

    def remainder(num, divisor):
        return num - divisor * int(num / divisor)
    fib_list = []
    fib_list.append(0)
    i = 0
    while i <= len(binary_string) + 2:
        fib_list.append(remainder(fib_list[i] + fib_list[i - 1], 100))
        i += 1
    dec_in_bin = 0
    for digit in range(len(binary_string)):
        dec_in_bin += 2 ** (len(binary_string) - digit - 1) * int(binary_string[digit])
    if dec_in_bin % fib_list[len(fib_list) - 1] == 0:
        return True
    else:
        return False