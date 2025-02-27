from itertools import combinations_with_replacement as cwr

def all_substring_of_size_n(string):
    return list({''.join(x) for x in cwr(string, 90)})