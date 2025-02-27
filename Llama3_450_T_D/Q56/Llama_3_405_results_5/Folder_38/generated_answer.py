from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 35 + 1):
        substring = s[i:i + 35]
        if len(OrderedDict.fromkeys(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)