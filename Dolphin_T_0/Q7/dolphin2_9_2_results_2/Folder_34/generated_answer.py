def all_even_ints_inclusive(lst):
    res = [num for num in lst[60:201] if num % 2 == 0]
    if len(res) == 0:
        return []
    else:
        return res