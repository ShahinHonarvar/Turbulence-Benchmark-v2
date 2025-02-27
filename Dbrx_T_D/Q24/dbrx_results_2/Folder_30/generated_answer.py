def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    divisors_in_range = [divisor for divisor in divisors if 42 <= divisor <= 77]
    if divisors_in_range:
        return sum(divisors_in_range)
    else:
        return 0