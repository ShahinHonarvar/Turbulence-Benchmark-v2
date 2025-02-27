def is_positive_divisor(number, divisor):
    if number < 0 or divisor < 0:
        raise ValueError('Both number and divisor must be positive.')
    return number % divisor == 0

def get_divisors(number):
    divisors = set()
    for i in range(1, number + 1):
        if is_positive_divisor(number, i):
            divisors.add(i)
    return divisors

def sum_of_divisors_in_range(number):
    divisors = get_divisors(number)
    return sum((divisor for divisor in divisors if 157 <= divisor <= 902))