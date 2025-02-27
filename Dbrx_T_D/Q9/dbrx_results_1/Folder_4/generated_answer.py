def all_odd_ints_inclusive(input_list):
    if len(input_list) < 92:
        return []
    odd_ints = [i for i in input_list[12:93] if i % 2 != 0]
    return odd_ints