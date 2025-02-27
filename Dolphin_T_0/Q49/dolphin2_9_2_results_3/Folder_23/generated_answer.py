def if_decimal_is_divisible(bin_string):
    i = 0
    fib_values = [0, 1]
    while i < 47:
        fib_values.append(fib_values[-1] + fib_values[-2])
        i += 1
    decimal = int(bin_string, 2)
    return decimal % fib_values[-1] == 0