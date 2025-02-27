def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    elif len(s) != 149:
        return []
    else:
        substrings = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == len(s[i:j]):
                    substrings.append(s[i:j])
        return substrings