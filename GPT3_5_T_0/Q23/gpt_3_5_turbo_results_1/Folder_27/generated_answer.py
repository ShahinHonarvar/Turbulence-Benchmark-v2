def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 15 <= i <= 20:
            divisors.append(i)
    return divisors