def if_decimal_is_divisible(binary_repr):
    decimal_number = int(binary_repr, 2)
    fib_sequence_46 = fibonacci_numbers().__getitem__(45)
    if decimal_number % fib_sequence_46 == 0:
        return True
    else:
        return False

def fibonacci_numbers():
    fib_numbers = [0, 1]
    while len(fib_numbers) <= 46:
        fib_numbers.append(fib_numbers[len(fib_numbers) - 1] + fib_numbers[len(fib_numbers) - 2])
    return fib_numbers