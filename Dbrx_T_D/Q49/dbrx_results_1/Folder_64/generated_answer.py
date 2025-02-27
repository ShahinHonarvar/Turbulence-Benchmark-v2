def is_fibonacci(number):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] < number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1] == number

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    return is_fibonacci(decimal_number) and decimal_number % 55 == 0