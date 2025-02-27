def find_divisors_in_range(n):
    divisors = []
    for i in range(11, 57):
        if n % i == 0 and i != n:
            divisors.append(i)
    return divisors