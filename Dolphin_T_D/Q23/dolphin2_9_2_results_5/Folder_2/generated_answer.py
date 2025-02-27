def find_divisors_in_range(num):
    divisors = []
    lower = 315
    upper = 955
    for i in range(lower, upper + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors