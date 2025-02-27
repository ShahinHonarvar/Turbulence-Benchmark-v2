from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(OrderedDict.fromkeys(substring)) == 24:
            substrings.add(substring)
    return list(substrings)