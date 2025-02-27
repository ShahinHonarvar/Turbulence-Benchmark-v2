def find_divisors_in_range(given_number):
    list_of_divisors = []
    for i in range(2, 7):
        if given_number % i == 0:
            list_of_divisors.append(i)
    if len(list_of_divisors) == 0:
        return []
    return list_of_divisors