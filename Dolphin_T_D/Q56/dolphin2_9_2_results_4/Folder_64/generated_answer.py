def all_substring_of_size_n(s):
    return [''.join(i) for i in set([s[j:j + 8] for j in range(len(s)) if len(set(s[j:j + 8])) == 8])]