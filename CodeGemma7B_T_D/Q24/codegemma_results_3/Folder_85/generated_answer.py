def sum_of_divisors_in_range(number):
    total = 0
    for i in range(2, number + 1):
        if number % i == 0:
            if i >= 2 and i <= 5:
                total += i
    return total