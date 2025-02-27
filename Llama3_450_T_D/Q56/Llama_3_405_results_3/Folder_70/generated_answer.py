from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            substrings.add(''.join(OrderedDict.fromkeys(substring)))
    return list(substrings)