def sum_of_divisors_in_range(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    sub_divisors = []
    for divisor in divisors:
        if 10 <= divisor <= 55:
            sub_divisors.append(divisor)
    if sub_divisors:
        return sum(sub_divisors)
    else:
        return 0