def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisors_in_range = [i for i in divisors if 15 <= i <= 92]
    return sum(divisors_in_range) if divisors_in_range else 0