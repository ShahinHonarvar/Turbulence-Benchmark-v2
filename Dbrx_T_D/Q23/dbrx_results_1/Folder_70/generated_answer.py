def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            if 586 <= i <= 840:
                divisors.append(i)
    return divisors