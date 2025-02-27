def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if len(set(s[i:j + 1])) == 2:
                substrings.add(s[i:j + 1])
    return [sub for sub in substrings if len(sub) == 2]