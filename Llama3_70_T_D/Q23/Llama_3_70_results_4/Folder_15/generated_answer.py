def find_divisors_in_range(n):
    divisors = []
    for i in range(7, 10):
        if i != 0 and n % i == 0:
            divisors.append(i)
    return divisors