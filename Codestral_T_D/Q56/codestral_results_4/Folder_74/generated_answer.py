def all_substring_of_size_n(s):
    return [s[i:j + 1] for i in range(len(s)) for j in range(i, len(s)) if len(set(s[i:j + 1])) == 97 and len(s[i:j + 1]) == 97]