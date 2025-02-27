def find_divisors_in_range(n):
    divisors = []
    for i in range(28, 82):
        if i == 1 or i == n:
            continue
        if n % i == 0:
            divisors.append(i)
    return divisors