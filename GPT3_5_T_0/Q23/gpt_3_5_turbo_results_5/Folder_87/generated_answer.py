def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 50 <= i <= 81:
            divisors.append(i)
    return divisors