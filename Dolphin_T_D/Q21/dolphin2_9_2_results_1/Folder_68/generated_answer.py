def all_ints_div_by_num(integers):
    divisible = []
    for div in integers:
        if div % 8 == 0:
            divisible.append(div)
    return divisible