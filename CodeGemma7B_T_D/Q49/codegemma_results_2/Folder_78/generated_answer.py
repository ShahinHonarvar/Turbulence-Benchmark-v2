def if_decimal_is_divisible(binary_string):
    fib_seq = [0]
    num = int(binary_string, 2)
    index = 1
    while num >= fib_seq[-1]:
        fib_seq.append(fib_seq[index - 1] + fib_seq[index])
        index += 1
    return num % fib_seq[114] == 0