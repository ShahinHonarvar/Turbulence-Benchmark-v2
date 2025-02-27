def all_substring_of_size_n(s):
    return [''.join(sorted(set(s[i:i + 143]), key=s[i:i + 143].index)) for i in range(len(s) - 142) if len(set(s[i:i + 143])) == 143]