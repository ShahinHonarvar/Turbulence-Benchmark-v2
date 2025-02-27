def sum_of_divisors_in_range(number):
    sum = 0
    for i in range(2, 8):
        if number % i == 0:
            sum += i
    else:
        return 0
    return sum