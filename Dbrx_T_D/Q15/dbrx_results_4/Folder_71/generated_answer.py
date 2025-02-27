def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 53:
        return 'Input list should have at least 53 elements.'
    else:
        odd_ints = [i for i in integer_list[25:53] if i % 2 != 0]
        if not odd_ints:
            return 0
        else:
            return sum(odd_ints)