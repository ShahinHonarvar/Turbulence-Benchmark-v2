from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(OrderedDict.fromkeys(substring)) == 40:
            substrings.add(substring)
    return list(substrings)