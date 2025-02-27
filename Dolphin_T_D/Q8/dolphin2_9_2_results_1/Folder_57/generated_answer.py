def all_even_ints_exclusive(lst):
    result = []
    for num in lst[19:37]:
        if num % 2 == 0:
            result.append(num)
    return result