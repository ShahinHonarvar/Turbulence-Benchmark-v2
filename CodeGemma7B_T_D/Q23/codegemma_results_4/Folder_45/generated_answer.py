def find_divisors_in_range(n):
    divisors = []
    if n > 3 and n < 9:
        for i in range(4, n + 1):
            if n % i == 0:
                divisors.append(i)
    return divisors