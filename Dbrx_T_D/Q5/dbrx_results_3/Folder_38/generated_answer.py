def all_neg_ints_inclusive(input_list):
    if not isinstance(input_list, list):
        raise ValueError('Input must be a list')
    if len(input_list) < 63 or len(input_list) > 63:
        return []
    return [i for i in input_list[22:64] if i < 0]