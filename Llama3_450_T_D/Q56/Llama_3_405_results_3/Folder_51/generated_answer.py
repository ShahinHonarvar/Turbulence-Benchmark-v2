from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if len(OrderedDict.fromkeys(substring)) == 96:
            substrings.add(substring)
    return list(substrings)