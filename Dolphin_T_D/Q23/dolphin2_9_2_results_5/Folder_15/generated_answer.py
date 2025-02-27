def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if i % 2 != 0 and n % i == 0:
            divisors.append(i)
    return divisors