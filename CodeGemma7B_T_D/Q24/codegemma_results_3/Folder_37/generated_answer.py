def sum_of_divisors_in_range(num):
    divisors = [i for i in range(3, 8) if num % i == 0]
    if not divisors:
        return 0
    return sum(divisors)