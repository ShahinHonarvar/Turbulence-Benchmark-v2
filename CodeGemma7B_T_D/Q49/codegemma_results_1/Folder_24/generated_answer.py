def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    while fib[-1] <= int(binary_representation, 2):
        fib.append(fib[-1] + fib[-2])
    return int(binary_representation, 2) in [x for x in fib if x % 56 == 0]