from itertools import product

def all_substring_of_size_n(string):
    result = []
    for substring in product(string, repeat=71):
        if len(substring) == 71 and len(set(substring)) == 71:
            result.append(''.join(substring))
    return result