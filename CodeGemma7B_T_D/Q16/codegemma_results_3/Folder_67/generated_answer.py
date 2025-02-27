def sum_even_ints_inclusive(list):
    total = 0
    range_a, range_b = (22, 50)
    if min(range_a, range_b) <= min((i for i in list if i % 2 == 0)) and max(range_b, range_a) >= max((i for i in list if i % 2 == 0)):
        for i in list[range_a:range_b + 1]:
            if i % 2 == 0:
                total += i
    return total