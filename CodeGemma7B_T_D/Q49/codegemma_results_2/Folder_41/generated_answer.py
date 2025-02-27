def if_decimal_is_divisible(bin_repres):
    bin_repres = list(reversed(bin_repres))
    fib = 1
    first = True
    dec = 0
    for i in bin_repres:
        if i == '1':
            if first:
                fib += 1
                first = False
            dec += 2 ** fib
    return dec % 67 == 0