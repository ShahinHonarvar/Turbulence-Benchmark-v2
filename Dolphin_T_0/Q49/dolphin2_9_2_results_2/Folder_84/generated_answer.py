def if_decimal_is_divisible(binary):
    fib_seq = [0, 1]
    index = 2
    while index < 196:
        fib_seq.append(fib_seq[index - 1] + fib_seq[index - 2])
        index += 1
    num = int(binary, 2)
    if num % fib_seq[195] == 0:
        return True
    else:
        return False