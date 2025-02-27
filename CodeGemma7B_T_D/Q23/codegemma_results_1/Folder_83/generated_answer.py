def find_divisors_in_range(num):
    if num <= 0 and num >= 10:
        return []
    list_of_divisors = []
    for i in range(5, 8):
        if num % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors