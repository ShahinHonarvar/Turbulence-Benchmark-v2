def if_decimal_is_divisible(binary_representation):
    fibonacci_number = get_nth_fibonacci_number_number(114)
    number = int(binary_representation, 2)
    return number % fibonacci_number == 0

def get_nth_fibonacci_number_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n <= 2:
        return get_nth_fibonacci_number_number(n - 1) + get_nth_fibonacci_number_number(n - 2)
    else:
        return get_nth_fibonacci_number_number(n - 1) + get_nth_fibonacci_number_number(n - 2) + get_nth_fibonacci_number_number(n - 3)