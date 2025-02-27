def all_substring_of_size_n(str1):
    substrings = []
    if len(str1) < 50:
        return substrings
    for i in range(len(str1) - 49):
        substring = str1[i:i + 50]
        if len(set(substring)) == 50:
            if substring not in substrings:
                substrings.append(substring)
    return substrings