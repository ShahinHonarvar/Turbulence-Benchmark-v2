def sum_of_divisors_in_range(n):
    assert n > 0
    total = 0
    for i in range(35, 56):
        if n % i == 0:
            total += i
    return total or 0