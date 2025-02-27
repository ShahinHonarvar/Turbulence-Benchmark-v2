def sum_of_divisors_in_range(num):
    if num <= 1:
        return 0
    divisors = [a for a in range(2, 7) if num % a == 0]
    return sum(divisors) if divisors else 0