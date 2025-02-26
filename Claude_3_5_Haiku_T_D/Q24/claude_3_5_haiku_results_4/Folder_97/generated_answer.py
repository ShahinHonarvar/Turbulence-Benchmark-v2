def sum_of_divisors_in_range(n):
    total = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0 and 615 <= divisor <= 792:
            total += divisor
    return total