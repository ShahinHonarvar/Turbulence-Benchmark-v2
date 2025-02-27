from collections import OrderedDict

def all_substring_of_size_n(s):
    unique_substrings = set()
    substring_size = 127
    for i in range(len(s) - substring_size + 1):
        substring = s[i:i + substring_size]
        if len(set(substring)) == substring_size:
            unique_substrings.add(substring)
    return list(unique_substrings)