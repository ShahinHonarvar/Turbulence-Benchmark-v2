def all_substring_of_size_n(s):
    out = []
    for i in range(len(s)):
        if len(s[i:i + 67]) == 67:
            if s[i:i + 67] not in out:
                out.append(s[i:i + 67])
    return out