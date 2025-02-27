def sum_of_divisors_in_range(n):
    divisors_in_range = [i for i in range(1, n + 1) if n % i == 0 and 71 <= i <= 81]
    return sum(divisors_in_range)