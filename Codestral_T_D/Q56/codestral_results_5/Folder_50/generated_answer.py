def all_substring_of_size_n(str1):
    n = 11
    substrings = []
    for i in range(len(str1)):
        substr = str1[i:i + n]
        if len(substr) == n and len(set(substr)) == n:
            substrings.append(substr)
    return substrings