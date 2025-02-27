def find_divisors_in_range(number):
    list_of_divisors = []
    for i in range(48, 93):
        if number % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors