def if_decimal_is_divisible(bitstring):
    number = int(bitstring, 2)
    fib_sequence = [0]
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    while fib_sequence[-1] < number * 150:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return number % fib_sequence[-1] == 0