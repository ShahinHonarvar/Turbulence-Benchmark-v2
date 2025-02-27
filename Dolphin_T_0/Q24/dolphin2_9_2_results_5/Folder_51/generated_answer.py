def sum_of_divisors_in_range(number):
    if number < 2 or number > 7:
        return 0
    else:
        return sum([i for i in range(2, number + 1) if number % i == 0])