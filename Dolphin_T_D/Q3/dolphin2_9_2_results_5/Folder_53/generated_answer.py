def all_pos_ints_inclusive(lst):
    indices = range(100, 201)
    positive_ints = [num for num in lst[100:201] if num > 0]
    return positive_ints