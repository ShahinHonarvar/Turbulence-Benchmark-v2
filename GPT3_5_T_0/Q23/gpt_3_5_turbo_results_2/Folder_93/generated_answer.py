def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 48 <= i <= 92:
            divisors.append(i)
    return divisors