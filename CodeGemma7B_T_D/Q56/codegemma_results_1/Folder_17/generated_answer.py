from itertools import combinations_with_replacement as cwr

def all_substring_of_size_n(string):
    result = set((''.join(i) for i in cwr(string, 37)))
    return list(filter(lambda x: len(x) == 37 and len(set(x)) == 37, result))