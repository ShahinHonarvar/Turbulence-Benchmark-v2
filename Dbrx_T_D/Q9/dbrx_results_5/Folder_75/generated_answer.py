def all_odd_ints_inclusive(lst):
    if not isinstance(lst, list) or len(lst) < 58:
        return []
    odd_ints = [i for i in lst[56:58] if isinstance(i, int) and i % 2 != 0]
    return odd_ints