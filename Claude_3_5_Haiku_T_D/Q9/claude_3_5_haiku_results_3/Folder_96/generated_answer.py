def all_odd_ints_inclusive(lst):
    if len(lst) <= 200:
        return []
    return [num for num in lst[50:201] if num % 2 != 0]