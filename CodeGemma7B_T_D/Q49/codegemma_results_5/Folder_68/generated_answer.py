def if_decimal_is_divisible(string):
    fib_list = [0, 1]
    length = len(string)
    for i in range(2, 38):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    decimal = int(string, 2)
    if decimal % fib_list[37] == 0:
        return True
    else:
        return False