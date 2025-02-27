def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s)):
        if len(set(s[i:i + 12])) == 12:
            subs.append(s[i:i + 12])
    return subs