from collections import OrderedDict

def all_substring_of_size_n(s):

    def has_duplicate(string):
        return len(string) != len(OrderedDict.fromkeys(string))
    substrings = [s[i:i + 64] for i in range(len(s) - 63) if not has_duplicate(s[i:i + 64])]
    return list(set(substrings))