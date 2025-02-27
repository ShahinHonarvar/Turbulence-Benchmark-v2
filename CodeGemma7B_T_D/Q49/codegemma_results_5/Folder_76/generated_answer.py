def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    current_index = 2
    while fib[-1] < 1000000000000000000:
        fib.append(fib[current_index - 1] + fib[current_index - 2])
        current_index += 1
    decimal = int(binary_representation, 2)
    return decimal % fib[188] == 0