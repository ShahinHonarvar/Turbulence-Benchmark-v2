def sum_odd_ints_inclusive(int_list):
    if len(int_list) >= 36:
        odds = [i for i in int_list[31:36] if i % 2 != 0]
        return sum(odds) if odds else 0
    else:
        return 'List is too short'