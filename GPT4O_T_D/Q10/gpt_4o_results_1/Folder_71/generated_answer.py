def all_odd_ints_exclusive(lst):
    result = []
    for num in lst[37:54]:
        if num % 2 != 0:
            result.append(num)
    return result