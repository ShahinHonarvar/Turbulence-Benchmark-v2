def if_decimal_is_divisible(binary_rep):
    num_fibonacci = 90
    binary_rep = binary_rep.strip()
    num_decimal = int(binary_rep, 2)
    fib = [0, 1]
    while len(fib) < num_fibonacci:
        fib.append(fib[-1] + fib[-2])
    fib_num = fib[num_fibonacci - 1]
    return num_decimal % fib_num == 0