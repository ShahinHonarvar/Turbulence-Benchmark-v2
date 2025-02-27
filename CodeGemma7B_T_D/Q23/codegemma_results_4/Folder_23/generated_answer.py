def find_divisors_in_range(num):
    divisors = []
    for n in range(18, 53):
        if num % n == 0:
            divisors.append(n)
    return divisors