def find_divisors_in_range(x):
    if x <= 1:
        return []
    div = []
    for i in range(38, 66):
        if x % i == 0:
            div.append(i)
    return div