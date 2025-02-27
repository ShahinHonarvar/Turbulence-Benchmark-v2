def if_decimal_is_divisible(binary_representation):
    binary_to_decimal = int(binary_representation, 2)
    fib_number = get_fib_number(binary_to_decimal)
    return binary_to_decimal % fib_number == 0

def get_fib_number(number):
    fib_sequence = [0]
    current_number = 1
    while current_number <= number:
        fib_sequence.append(current_number)
        current_number = fib_sequence[-1] + fib_sequence[-2]
    fib_number = fib_sequence[80]
    return fib_number