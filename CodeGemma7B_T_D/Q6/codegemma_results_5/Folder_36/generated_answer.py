def all_neg_ints_exclusive(lst):
    result = []
    for num in lst[598:767]:
        if num < 0:
            result.append(num)
    return result