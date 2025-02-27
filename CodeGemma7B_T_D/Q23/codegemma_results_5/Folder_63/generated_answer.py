def find_divisors_in_range(int):
    divs = []
    for i in range(39, 44):
        if num % i == 0:
            divs.append(i)
    return divs