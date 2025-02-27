def all_pos_ints_inclusive(lst):
    valid_index = [0, 1, 2]
    positive_integers = [num for num in lst if num > 0]
    return [positive_integers[i] for i in valid_index if i < len(positive_integers)]