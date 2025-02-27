from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if len(OrderedDict.fromkeys(substring)) == 46:
            substrings.add(substring)
    return list(substrings)