def sum_odd_ints_inclusive(lst):
    if not any((num % 2 for num in lst[62:79])):
        return 0
    return sum((num for num in lst[62:79] if num % 2))