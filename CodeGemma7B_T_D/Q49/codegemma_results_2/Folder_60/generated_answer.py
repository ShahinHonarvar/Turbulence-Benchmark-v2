from libnum.bn import BigNumber

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % 2 == 0:
        return True
    previous_fibonacci_number = BigNumber(1)
    current_fibonacci_number = BigNumber(1)
    for _ in range(106):
        next_fibonacci_number = previous_fibonacci_number + current_fibonacci_number
        previous_fibonacci_number = current_fibonacci_number
        current_fibonacci_number = next_fibonacci_number
    if decimal_integer % current_fibonacci_number == 0:
        return True
    return False