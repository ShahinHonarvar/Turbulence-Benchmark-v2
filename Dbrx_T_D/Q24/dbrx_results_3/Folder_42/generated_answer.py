def sum_of_divisors_in_range(n):
    divisors = set()
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            divisors.add(divisor)
    divisors_in_range = [divisor for divisor in divisors if 14 <= divisor <= 93]
    return sum(divisors_in_range) if divisors_in_range else 0