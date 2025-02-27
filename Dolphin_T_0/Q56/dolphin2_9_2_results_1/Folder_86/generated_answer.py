def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    subs = [s[i:i + 143] for i in range(len(s)) if len(set(s[i:i + 143])) == 143]
    return list(set(subs))