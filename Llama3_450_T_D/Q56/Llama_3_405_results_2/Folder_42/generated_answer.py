from collections import OrderedDict

def all_substring_of_size_n(s):

    def has_no_duplicates(substring):
        return len(OrderedDict.fromkeys(substring)) == len(substring)
    substrings = [s[i:i + 45] for i in range(len(s) - 44)]
    return list(set([substring for substring in substrings if has_no_duplicates(substring)]))