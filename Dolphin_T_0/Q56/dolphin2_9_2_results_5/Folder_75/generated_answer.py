def all_substring_of_size_n(s):
    substr = set()
    for i in range(len(s) - 15):
        s16 = s[i:i + 16]
        if len(set(s16)) == 16:
            substr.add(s16)
    return list(substr)