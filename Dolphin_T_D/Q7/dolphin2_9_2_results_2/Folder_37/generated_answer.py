def all_even_ints_inclusive(lst):
    result = []
    for number in lst[1:6]:
        if number % 2 == 0:
            result.append(number)
    return result