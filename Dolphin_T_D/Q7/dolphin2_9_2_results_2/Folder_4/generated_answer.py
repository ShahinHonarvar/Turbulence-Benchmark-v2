def all_even_ints_inclusive(lst):
    result = []
    for num in lst[12:93]:
        if num % 2 == 0:
            result.append(num)
    return result