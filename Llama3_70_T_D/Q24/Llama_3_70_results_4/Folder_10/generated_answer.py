def sum_of_divisors_in_range(num):
    divisors = [i for i in range(60, 87) if num % i == 0]
    return sum(divisors)