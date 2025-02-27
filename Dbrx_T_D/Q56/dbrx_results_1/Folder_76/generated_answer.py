from collections import OrderedDict

def all_substring_of_size_n(s):
    result = []
    if len(s) < 149:
        return result
    for i in range(len(s) - 149 + 1):
        substring = s[i:i + 149]
        if len(OrderedDict.fromkeys(substring)) == 149:
            result.append(substring)
    return list(set(result))