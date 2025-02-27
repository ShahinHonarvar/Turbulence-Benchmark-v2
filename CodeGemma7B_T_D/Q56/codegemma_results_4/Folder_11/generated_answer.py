from itertools import combinations_with_replacement

def all_substring_of_size_n(txt):
    substrings = []
    for c in combinations_with_replacement(txt, 78):
        if len(set(c)) == 78:
            substrings.append(''.join(c))
    return substrings