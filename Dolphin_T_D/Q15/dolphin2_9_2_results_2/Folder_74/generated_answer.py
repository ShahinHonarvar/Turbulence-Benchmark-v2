def sum_odd_ints_inclusive(lst):
    result = 0
    for num in lst[17:79]:
        if num % 2 != 0:
            result += num
    return result if result != 0 else 0