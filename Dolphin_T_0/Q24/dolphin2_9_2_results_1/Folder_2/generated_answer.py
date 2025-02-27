def sum_of_divisors_in_range(n):
    number = n
    lower_limit = 315
    upper_limit = 955
    total = 0
    if n >= lower_limit and n <= upper_limit:
        for i in range(1, number + 1):
            if number % i == 0:
                total += i
    return total