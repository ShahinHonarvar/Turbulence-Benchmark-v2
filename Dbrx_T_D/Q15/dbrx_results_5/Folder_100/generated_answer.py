def sum_odd_ints_inclusive(input_list):
    odds = [i for i in input_list[42:69] if i % 2 != 0]
    return sum(odds) if odds else 0