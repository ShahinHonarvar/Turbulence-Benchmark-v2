def find_divisors_in_range(num):
    if num > 0 and num % 2 == 0:
        start = 60
    else:
        start = 61
    end = 86
    dividers = []
    for i in range(start, end + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers