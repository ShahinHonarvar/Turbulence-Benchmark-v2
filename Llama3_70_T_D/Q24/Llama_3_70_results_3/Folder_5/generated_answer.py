def sum_of_divisors_in_range(number):
    if number < 1:
        raise ValueError('Input number must be a positive integer')
    sum = 0
    for i in range(1, number + 1):
        if number % i == 0 and 7 <= i <= 8:
            sum += i
    return sum