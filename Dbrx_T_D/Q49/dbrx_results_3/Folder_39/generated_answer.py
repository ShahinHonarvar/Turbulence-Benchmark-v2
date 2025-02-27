def is_fibonacci(number):
    if number == 0 or number == 1 or number == 2:
        return True
    fib_sequence = [0, 1, 2]
    while fib_sequence[-1] + fib_sequence[-2] < number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return number == fib_sequence[-1]

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_number = 15
    while not is_fibonacci(fib_number):
        fib_number += 1
    return decimal_number % fib_number == 0