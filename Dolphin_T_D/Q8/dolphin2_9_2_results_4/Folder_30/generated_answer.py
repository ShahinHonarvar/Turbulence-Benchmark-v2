def all_even_ints_exclusive(lst):
    if 86 < len(lst) < 90:
        return [num for num in lst[87:90] if num % 2 == 0]
    else:
        return []