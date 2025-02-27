from collections import OrderedDict

def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if len(set(substring)) == 95:
            unique_substrings.add(substring)
    return list(unique_substrings)