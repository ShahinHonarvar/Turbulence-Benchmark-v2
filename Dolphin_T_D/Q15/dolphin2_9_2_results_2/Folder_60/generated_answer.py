def sum_odd_ints_inclusive(lst):
    result = 0
    for num in lst[75:86]:
        if num % 2 != 0:
            result += num
    return result