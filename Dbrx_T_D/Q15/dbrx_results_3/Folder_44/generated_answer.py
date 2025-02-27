def sum_odd_ints_inclusive(int_list):
    odds = [i for i in int_list[13:69] if i % 2 != 0]
    return sum(odds) if odds else 0