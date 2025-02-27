def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_numbers = set()
    current, next = (0, 1)
    for _ in range(97):
        current, next = (next, current + next)
        fibonacci_numbers.add(current)
    return decimal_integer % 97 in fibonacci_numbers