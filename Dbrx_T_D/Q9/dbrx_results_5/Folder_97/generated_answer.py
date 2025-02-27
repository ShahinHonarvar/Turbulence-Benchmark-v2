def all_odd_ints_inclusive(lst):
    if len(lst) < 80:
        return []
    odd_ints = [i for i in lst[40:81] if i % 2 != 0]
    return odd_ints