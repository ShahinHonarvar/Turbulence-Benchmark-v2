def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    for _ in range(109):
        fib.append(fib[-1] + fib[-2])
    fibbinach_numbers = bin(fib[-1])[2:].zfill(len(binary_representation))
    while len(fibbinach_numbers) > len(binary_representation):
        fibbinach_numbers = fibbinach_numbers[1:]
    return int(fibbinach_numbers, 2) % int(binary_representation, 2) == 0