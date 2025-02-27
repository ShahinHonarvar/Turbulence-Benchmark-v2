def sum_of_divisors_in_range(n):
    sum_divisors = 0
    for i in range(1, 49):
        if n % i == 0 and 14 <= i <= 48:
            sum_divisors += i
    return sum_divisors