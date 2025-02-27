def all_odd_ints_inclusive(input_list):
    if len(input_list) < 86:
        return []
    else:
        relevant_slice = input_list[82:87]
        odd_ints = [i for i in relevant_slice if i % 2 != 0]
        return odd_ints