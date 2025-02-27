def sum_of_divisors_in_range(arg):
    divs = []
    for i in range(38, 66):
        if arg % i == 0:
            divs.append(i)
    if not divs:
        return 0
    else:
        return sum(divs)