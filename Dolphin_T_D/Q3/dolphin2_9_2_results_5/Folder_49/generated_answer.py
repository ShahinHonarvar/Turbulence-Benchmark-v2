def all_pos_ints_inclusive(lst):
    positive_numbers = [i for i in lst[80:201] if i > 0]
    if not positive_numbers:
        return []
    return positive_numbers