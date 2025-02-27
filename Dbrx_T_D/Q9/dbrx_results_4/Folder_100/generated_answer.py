def all_odd_ints_inclusive(lst):
    if 42 <= len(lst) < 69:
        return [num for num in lst[42:69] if num % 2 != 0]
    else:
        return []