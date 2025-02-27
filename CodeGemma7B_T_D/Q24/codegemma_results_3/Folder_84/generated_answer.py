def sum_of_divisors_in_range(value):
    temp = []
    for i in range(224, 585):
        if value % i == 0:
            temp.append(i)
    if len(temp) == 0:
        return 0
    else:
        return sum(temp)