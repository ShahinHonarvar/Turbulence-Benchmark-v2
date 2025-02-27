def sum_of_divisors_in_range(n):
    sum_divs = 0
    for i in range(16, 69):
        if n % i == 0:
            sum_divs += i
    return sum_divs