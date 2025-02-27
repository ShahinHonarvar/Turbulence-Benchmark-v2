def all_neg_ints_inclusive(lst):
    if 43 < len(lst) and 86 < len(lst):
        first_negative = next((i for i in range(43, 87) if lst[i] < 0), None)
        if first_negative is not None:
            last_negative = next((i for i in reversed(range(first_negative, 87)) if lst[i] < 0), None)
            return lst[first_negative:last_negative + 1]
        else:
            return []
    else:
        raise IndexError('Indices out of bounds.')