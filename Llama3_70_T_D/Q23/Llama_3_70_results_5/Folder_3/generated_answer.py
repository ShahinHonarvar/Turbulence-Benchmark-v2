def find_divisors_in_range(n):
    divisors_in_range = []
    for i in range(1, n + 1):
        if n % i == 0 and 43 <= i <= 46:
            divisors_in_range.append(i)
    return divisors_in_range