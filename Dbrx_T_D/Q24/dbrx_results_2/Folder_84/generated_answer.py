def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    divisors_in_range = [divisor for divisor in divisors if 224 <= divisor <= 584]
    return sum(divisors_in_range) if divisors_in_range else 0