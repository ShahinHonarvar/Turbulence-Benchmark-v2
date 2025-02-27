def sum_even_ints_inclusive(integers):
    if 667 <= 774 < len(integers):
        return sum(filter(lambda x: x % 2 == 0, integers[667:775]))
    else:
        return 0