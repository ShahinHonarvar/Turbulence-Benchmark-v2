def if_decimal_is_divisible(binary):
    fib_check = 80
    fib_list = [0, 1]
    while fib_list[-1] < fib_check:
        fib_list.append(fib_list[-1] + fib_list[-2])
    p_fib = [0]
    while fib_list[-1] > 2 ** (len(binary) - 1):
        p_fib.append((fib_list[-2], fib_list[-1]))
        fib_list.pop()
    p_fib.append((fib_list[-2], fib_list[-1]))
    for term in p_fib:
        if term[1] == int(binary, 2):
            return True
    return False