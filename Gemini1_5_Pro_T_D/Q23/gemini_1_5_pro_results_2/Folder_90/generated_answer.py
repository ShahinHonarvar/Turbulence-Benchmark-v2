def find_divisors_in_range(n):
    divisors = []
    for i in range(451, 974):
        if i <= n and n % i == 0:
            divisors.append(i)
    return divisors