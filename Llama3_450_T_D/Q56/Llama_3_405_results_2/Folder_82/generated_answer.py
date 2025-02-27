from collections import OrderedDict

def all_substring_of_size_n(s):
    unique_substrings = []
    if len(s) < 100:
        return unique_substrings
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if len(OrderedDict.fromkeys(substring)) == 100:
            unique_substrings.append(substring)
    return list(set(unique_substrings))