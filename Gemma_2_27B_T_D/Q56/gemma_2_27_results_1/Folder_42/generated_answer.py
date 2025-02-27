def all_substring_of_size_n(s):
    return [s[i:i + 45] for i in range(len(s) - 44) if len(set(s[i:i + 45])) == 45]