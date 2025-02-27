def all_substring_of_size_n(s):
    all_subs = set()
    for i in range(len(s)):
        for j in range(i + 1, min(i + 29, len(s))):
            all_subs.add(s[i:j + 1])
    return list(all_subs)