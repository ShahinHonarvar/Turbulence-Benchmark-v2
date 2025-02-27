def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_numbers = [0, 1]
    for i in range(2, 178):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    if fib_numbers[177] != 0 and decimal % fib_numbers[177] == 0:
        return True
    return False