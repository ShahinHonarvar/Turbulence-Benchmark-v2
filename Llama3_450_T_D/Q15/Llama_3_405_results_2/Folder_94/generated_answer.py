def sum_odd_ints_inclusive(lst):
    if len(lst) <= 40:
        return sum([num for i, num in enumerate(lst) if 28 <= i <= 40 and num % 2 != 0])
    else:
        return sum([num for i, num in enumerate(lst[28:41]) if num % 2 != 0])