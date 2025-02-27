def if_decimal_is_divisible(binary):
    current_number = 0
    fib_counter = 1
    fib_number = 0
    while current_number != 154:
        fib_number = fib_number + fib_counter
        fib_counter += 1
        current_number += 1
    result = 0
    binary_reversed = binary[::-1]
    for digit in binary_reversed:
        digit = int(digit)
        result += digit * 2 ** fib_counter
        fib_counter -= 1
    if result % fib_number == 0:
        return True
    return False