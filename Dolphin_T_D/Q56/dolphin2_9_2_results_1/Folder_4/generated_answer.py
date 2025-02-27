def all_substring_of_size_n(s):
    substr = set()
    for i in range(len(s) - 40):
        sub = s[i:i + 41]
        if len(set(sub)) == len(sub):
            substr.add(sub)
    return list(substr)