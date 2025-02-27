def find_divisors_in_range(num):
    divisors = []
    for i in range(num):
        if i > 1 and num % i == 0:
            divisors.append(i)
    return divisors