def all_substring_of_size_n(s):
    n = 64
    if len(s) < n:
        return []
    substrings = {}
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        subs = ''.join(sorted(sub))
        if subs not in substrings:
            substrings[subs] = [sub]
        else:
            substrings[subs].append(sub)
    return [substrings[sub] for sub in substrings if len(substrings[sub]) > 1]