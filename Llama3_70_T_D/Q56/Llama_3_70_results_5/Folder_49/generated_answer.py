def all_substring_of_size_n(s):
    len_s = len(s)
    substrings = set()
    for i in range(len_s - 73 + 1):
        substr = s[i:i + 73]
        if len(set(substr)) == 73:
            substrings.add(substr)
    return list(substrings)