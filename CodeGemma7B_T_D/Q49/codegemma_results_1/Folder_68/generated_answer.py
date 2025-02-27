def if_decimal_is_divisible(binary_representation):
    sum = 0
    index = len(binary_representation) - 1
    fibonaccinumber = get_nth_fibonacci_number(38)
    for digit in binary_representation:
        if digit == '1':
            sum += 2 ** index
        index -= 1
    if sum % fibonaccinumber == 0:
        return True
    else:
        return False

def get_nth_fibonacci_number(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_nth_fibonacci_number(n - 1) + get_nth_fibonacci_number(n - 2)