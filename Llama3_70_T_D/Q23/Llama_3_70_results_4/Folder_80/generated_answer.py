def find_divisors_in_range(n):
    lower_bound = 70
    upper_bound = 93
    divisors_in_range = [i for i in range(lower_bound, upper_bound + 1) if n % i == 0]
    return divisors_in_range