def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    sum_divs = 0
    for i in range(224, 585):
        if num % i == 0:
            sum_divs += i
    return sum_divs