def if_decimal_is_divisible(binary_repr):
    fib_num = [0, 1]

    def get_fib_num(i):
        if i < len(fib_num):
            return fib_num[i]
        fib_num.append(get_fib_num(i - 1) + get_fib_num(i - 2))
        return fib_num[i]
    fib_num_34 = get_fib_num(33)
    if int('0b' + binary_repr, 2) % fib_num_34 == 0:
        return True
    else:
        return False