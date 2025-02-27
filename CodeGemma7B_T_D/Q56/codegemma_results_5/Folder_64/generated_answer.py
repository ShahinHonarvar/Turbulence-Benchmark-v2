def all_substring_of_size_n(s):
    list_substring = []
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            if len(set(s[start:end])) == 8:
                list_substring.append(s[start:end])
    return list_substring