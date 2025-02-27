def all_even_ints_inclusive(lst):
    result = []
    for x in range(lst[0], lst[-1] + 1):
        if x % 2 == 0:
            result.append(x)
    return result