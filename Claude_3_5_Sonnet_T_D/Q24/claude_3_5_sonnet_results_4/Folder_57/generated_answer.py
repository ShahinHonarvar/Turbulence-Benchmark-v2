def sum_of_divisors_in_range(number):
    total = 0
    for i in range(15, 93):
        if number % i == 0 and 15 <= i <= 92:
            total += i
    return total