def all_substring_of_size_n(str):
    substrings = []
    for i in range(len(str)):
        for j in range(i + 94, len(str) + 1):
            sub = str[i:j]
            if len(set(sub)) == 94:
                substrings.append(sub)
    return substrings