def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if 59 <= i <= 88:
                sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors