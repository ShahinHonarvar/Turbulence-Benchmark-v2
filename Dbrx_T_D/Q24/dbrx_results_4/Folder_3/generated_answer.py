def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    sum_of_divisors = sum((divisor for divisor in divisors if 43 <= divisor <= 46))
    return sum_of_divisors