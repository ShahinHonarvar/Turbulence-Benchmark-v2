def all_even_ints_exclusive(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and 276 < num < 376:
            result.append(num)
    return result