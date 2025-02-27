def all_pos_ints_exclusive(lst):
    positives = [num for num in lst[38:77] if num > 0]
    if not positives:
        return []
    else:
        return positives