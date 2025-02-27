def sum_of_divisors_in_range(index):
    all_divisors = []
    for i in range(39, 44):
        if index % i == 0:
            all_divisors.append(i)
    if len(all_divisors) == 0:
        return 0
    else:
        return sum(all_divisors)