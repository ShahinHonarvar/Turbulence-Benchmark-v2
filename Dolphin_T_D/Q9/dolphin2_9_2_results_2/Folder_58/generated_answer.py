def all_odd_ints_inclusive(lst):
    result = []
    for num in lst[209:557]:
        if num % 2 != 0:
            result.append(num)
    return result