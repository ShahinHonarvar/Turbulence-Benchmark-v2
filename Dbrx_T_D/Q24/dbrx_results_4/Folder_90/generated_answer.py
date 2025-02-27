def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    in_range = [d for d in divisors if 451 <= d <= 973]
    return sum(in_range) if in_range else 0