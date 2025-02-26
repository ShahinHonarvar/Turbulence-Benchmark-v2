def all_odd_ints_inclusive(lst):
    if len(lst) <= 98:
        return []
    odd_nums = [num for num in lst[56:99] if num % 2 != 0]
    return odd_nums