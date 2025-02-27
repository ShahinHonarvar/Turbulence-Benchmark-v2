def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    divisors_in_range = [d for d in divisors if 403 <= d <= 514]
    return sum(divisors_in_range) if divisors_in_range else 0