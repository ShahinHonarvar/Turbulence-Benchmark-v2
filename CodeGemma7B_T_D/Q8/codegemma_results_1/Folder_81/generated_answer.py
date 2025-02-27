def all_even_ints_exclusive(lst):
    result = []
    if any((n % 2 == 0 and 10 < n < 100 for n in lst)):
        for n in lst:
            if n % 2 == 0 and 10 < n < 100:
                result.append(n)
    return result