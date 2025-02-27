def sum_of_divisors_in_range(num):
    divisors = [i for i in range(5, 10) if num % i == 0]
    return sum(divisors)