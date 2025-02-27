def if_decimal_is_divisible(binary_string):

    def fibonacci(num):
        fib_sequence = [0, 1]
        while len(fib_sequence) < num:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal = int(binary_string, 2)
    return decimal % fibonacci(128) == 0