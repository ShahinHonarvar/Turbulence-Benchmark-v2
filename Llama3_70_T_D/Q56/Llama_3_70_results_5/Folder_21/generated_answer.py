def all_substring_of_size_n(s):
    return [''.join(set(sub)) for sub in set([''.join(sorted(s[i:i + 106])) for i in range(len(s) - 105)]) if len(set(sub)) == 106]