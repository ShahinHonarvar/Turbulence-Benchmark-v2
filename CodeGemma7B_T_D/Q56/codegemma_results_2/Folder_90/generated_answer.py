from itertools import combinations_with_replacement as cwr

def all_substring_of_size_n(s):
    size = 130
    ans = set(map(''.join, cwr(sorted(s), size)))
    return list(ans) if ans else []