def sum_of_divisors_in_range(num):
    divisors = [i for i in range(71, 82) if num % i == 0]
    return sum(divisors)