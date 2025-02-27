def sum_odd_ints_inclusive(integer_list):
    relevant_slice = integer_list[90:201]
    odd_ints = [i for i in relevant_slice if i % 2 != 0]
    if not odd_ints:
        return 0
    else:
        return sum(odd_ints)