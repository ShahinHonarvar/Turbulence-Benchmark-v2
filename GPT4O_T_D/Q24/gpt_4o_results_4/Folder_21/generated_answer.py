def sum_of_divisors_in_range(n):
    if n > 0:
        total = 0
        for i in range(120, 350):
            if n % i == 0:
                total += i
        return total
    return 0