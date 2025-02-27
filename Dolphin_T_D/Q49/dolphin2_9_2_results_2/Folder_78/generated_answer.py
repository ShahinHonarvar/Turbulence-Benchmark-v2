def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    index = 115
    fib = [0, 1]
    while len(fib) < index + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[index] != 0 and decimal_number % fib[index] == 0