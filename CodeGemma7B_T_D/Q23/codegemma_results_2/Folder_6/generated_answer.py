def find_divisors_in_range(num):
    if num <= 0 or num < 58:
        return []
    divisors = []
    for i in range(58, 91):
        if num % i == 0:
            divisors.append(i)
    return divisors