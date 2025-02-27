def sum_odd_ints_inclusive(int_list):
    start, end = (62, 63)
    odds = [i for i in int_list[start:end + 1] if i % 2 != 0]
    return sum(odds) if odds else 0