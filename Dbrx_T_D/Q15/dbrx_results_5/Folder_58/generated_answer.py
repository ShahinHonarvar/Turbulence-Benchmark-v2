def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 556:
        return 0
    odds = [i for i in int_list[209:557] if i % 2 != 0]
    return sum(odds) if odds else 0