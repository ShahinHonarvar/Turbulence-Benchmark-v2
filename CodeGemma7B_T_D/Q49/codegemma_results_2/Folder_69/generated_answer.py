def if_decimal_is_divisible(binary):
    fib, num, n = (0, 1, 0)
    finseq = []
    while len(finseq) <= 169:
        fib, num = (num, fib + num)
        n += 1
        finseq.append(fib)
    pos = int(binary, 2)
    divisible = False
    for num in finseq:
        if pos % num == 0:
            divisible = True
            break
    return divisible