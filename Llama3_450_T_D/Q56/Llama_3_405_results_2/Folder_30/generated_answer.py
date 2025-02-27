from collections import OrderedDict

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 78):
        sub = s[i:i + 79]
        if len(set(sub)) == 79:
            result.add(sub)
    return list(result)