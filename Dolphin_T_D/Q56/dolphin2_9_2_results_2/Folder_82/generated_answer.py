def all_substring_of_size_n(s):
    length = len(s)
    substrings = []
    for i in range(length):
        for j in range(i + 100, length + 1):
            if len(set(s[i:j])) == 100:
                substrings.append(s[i:j])
    return substrings if substrings != [] else []