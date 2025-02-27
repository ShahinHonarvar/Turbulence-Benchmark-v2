from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = OrderedDict()
        for j in range(i, len(s)):
            if s[j] in substring:
                break
            substring[s[j]] = None
            if len(substring) == 63:
                substrings.add(''.join(substring))
    return list(substrings)