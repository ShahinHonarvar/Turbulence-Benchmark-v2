def find_divisors_in_range(number):
    list = []
    for i in range(3, number):
        if number % i == 0:
            list.append(i)
    if len(list) == 0:
        return []
    else:
        return list