from collections import OrderedDict

def all_substring_of_size_n(s):

    def is_valid(sub):
        return len(OrderedDict.fromkeys(sub)) == 26
    substrings = set()
    for i in range(len(s) - 25):
        sub = s[i:i + 26]
        if is_valid(sub):
            substrings.add(sub)
    return list(substrings)