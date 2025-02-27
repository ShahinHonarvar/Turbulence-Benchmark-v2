def is_fibonacci(n):
    return n > 0 and n & n - 1 == 0

def fibonacci():
    current, next = (0, 1)
    while True:
        yield current
        current, next = (next, current + next)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if not is_fibonacci(decimal_integer):
        return False
    fibonacci_number = next((x for x in fibonacci() if x == 88))
    return decimal_integer % fibonacci_number == 0