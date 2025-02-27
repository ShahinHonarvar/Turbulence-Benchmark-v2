def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 126):
        substring = s[i:i + 127]
        if len(set(list(substring))) == 127:
            substrings.append(substring)
    return substrings