def sum_of_divisors_in_range(n):
    divisors = [i for i in range(2, int(n ** 0.5) + 1) if n % i == 0]
    filtered_divisors = [d for d in divisors if 46 <= d <= 65]
    return sum(filtered_divisors) or 0