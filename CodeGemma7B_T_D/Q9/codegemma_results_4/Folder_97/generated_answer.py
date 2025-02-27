def all_odd_ints_inclusive(li):
    if not li:
        return []
    return [x for x in li[40:81] if x % 2 != 0]