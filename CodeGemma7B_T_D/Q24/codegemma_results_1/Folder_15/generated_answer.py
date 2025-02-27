from re import match

def sum_of_divisors_in_range(number):
    if number <= 0:
        return 'Error: Number must be positive.'
    sum = 0
    for i in range(7, 10):
        if number % i == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum