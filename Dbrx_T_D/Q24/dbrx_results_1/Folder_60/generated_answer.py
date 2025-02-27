def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    sum_divisors = sum((div for div in divisors if 41 <= div <= 55))
    return sum_divisors if sum_divisors > 0 else 0