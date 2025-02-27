def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(4, 8):
        if n % i == 0:
            divisors.add(i)
    return sum(divisors)