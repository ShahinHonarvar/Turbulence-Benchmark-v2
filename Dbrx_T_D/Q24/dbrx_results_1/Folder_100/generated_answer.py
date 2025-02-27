def sum_of_divisors_in_range(n):
    divisors = list(range(1, min(n, 42)))
    for i in divisors:
        if n % i:
            divisors.remove(i)
    return sum(divisors)