def all_even_ints_inclusive(lst):
    if not any((i % 2 == 0 for i in lst[91:99 + 1])):
        return []
    return [i for i in lst[91:99 + 1] if i % 2 == 0]