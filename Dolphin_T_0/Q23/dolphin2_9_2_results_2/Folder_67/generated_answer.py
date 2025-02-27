def find_divisors_in_range(n):
    dividers = []
    for i in range(33, 58):
        if n % i == 0:
            dividers.append(i)
    return dividers