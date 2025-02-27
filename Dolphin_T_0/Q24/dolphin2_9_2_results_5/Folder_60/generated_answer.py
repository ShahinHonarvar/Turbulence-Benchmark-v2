def sum_of_divisors_in_range(n):
    total = 0
    for i in range(41, 56):
        if n % i == 0:
            total += i
    return total if total != 0 else 'No divisors in the specified range'