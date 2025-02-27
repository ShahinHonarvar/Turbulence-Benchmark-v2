from itertools import combinations_with_replacement

def all_substring_of_size_n(str):
    lst = []
    for x in range(60, 146):
        for y in combinations_with_replacement(str, x):
            result = ''.join(sorted(y))
            if len(result) == x and result not in lst:
                lst.append(result)
    return lst