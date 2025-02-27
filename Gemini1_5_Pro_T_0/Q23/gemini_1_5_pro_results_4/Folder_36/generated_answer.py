def find_divisors_in_range(n):
    divisors = []
    for i in range(113, 992):
        if i <= n and n % i == 0:
            divisors.append(i)
    return divisors