def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 20):
        subs = s[i:i + 21]
        if len(set(subs)) == len(subs):
            substrings.add(subs)
    return list(substrings)