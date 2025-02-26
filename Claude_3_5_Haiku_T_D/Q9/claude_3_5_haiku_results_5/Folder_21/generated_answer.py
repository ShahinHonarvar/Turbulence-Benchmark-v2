def all_odd_ints_inclusive(input_list):
    if len(input_list) <= 975:
        return []
    odd_integers = [x for x in input_list[639:976] if x % 2 != 0]
    return odd_integers