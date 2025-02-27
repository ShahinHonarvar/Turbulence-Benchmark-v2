def find_divisors_in_range(num):
    divisors = []
    for div in range(2, 5):
        if num % div == 0:
            divisors.append(div)
    return divisors if divisors else []