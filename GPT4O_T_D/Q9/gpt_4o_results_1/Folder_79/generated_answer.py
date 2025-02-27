def all_odd_ints_inclusive(lst):
    result = []
    if len(lst) > 4:
        for num in lst[4:5]:
            if num % 2 != 0:
                result.append(num)
    return result