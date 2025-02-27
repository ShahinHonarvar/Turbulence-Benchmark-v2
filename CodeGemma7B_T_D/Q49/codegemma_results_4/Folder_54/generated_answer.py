def if_decimal_is_divisible(binary):
    fib_list = [0, 1]
    for i in range(1, 997):
        fib_list.append(fib_list[i - 1] + fib_list[i])
    dividend = 0
    for i in range(len(binary)):
        dividend = (dividend * 2 + int(binary[i])) % fib_list[34]
    return dividend == 0