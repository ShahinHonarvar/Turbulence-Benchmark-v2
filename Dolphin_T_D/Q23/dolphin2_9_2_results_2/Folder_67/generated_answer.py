def find_divisors_in_range(n):
    divisors = []
    for divisor in range(33, 58):
        if n % divisor == 0:
            divisors.append(divisor)
    return divisors