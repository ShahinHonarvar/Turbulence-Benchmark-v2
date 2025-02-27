def all_substring_of_size_n(s):
    return [s[x:x + 86] for x in range(len(s)) if len(s[x:x + 86]) == 86 and len(set(s[x:x + 86])) == 86]