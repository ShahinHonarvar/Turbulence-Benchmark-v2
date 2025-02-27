def find_divisors_in_range(int):
    list = []
    for i in range(14, 49):
        if int % i == 0:
            list.append(i)
    return list