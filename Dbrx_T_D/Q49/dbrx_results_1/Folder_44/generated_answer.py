def is_decimal_divisible_by_159th_fibonacci_number(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = generate_fibonacci_number(159)
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False

def generate_fibonacci_number(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers[n - 1]