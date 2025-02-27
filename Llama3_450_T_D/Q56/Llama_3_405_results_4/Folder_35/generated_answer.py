from collections import OrderedDict

def all_substring_of_size_n(s):

    def check_unique(s):
        return len(OrderedDict.fromkeys(s)) == len(s)
    return list(set([s[i:i + 27] for i in range(len(s) - 26) if check_unique(s[i:i + 27])]))