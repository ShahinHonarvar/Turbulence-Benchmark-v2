def sum_of_divisors_in_range(n):
    divisors_sum = sum((i for i in range(35, 56) if n % i == 0))
    return divisors_sum if divisors_sum != 0 else 0