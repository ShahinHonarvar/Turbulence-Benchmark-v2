from collections import OrderedDict

def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 126):
        substring = s[i:i + 127]
        if len(OrderedDict.fromkeys(substring)) == 127:
            unique_substrings.add(substring)
    return list(unique_substrings)