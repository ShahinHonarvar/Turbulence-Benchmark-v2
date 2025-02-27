def sum_of_divisors_in_range(n):
    divisors = [div for div in range(1, n + 1) if n % div == 0]
    return sum([div for div in divisors if 228 <= div <= 846])