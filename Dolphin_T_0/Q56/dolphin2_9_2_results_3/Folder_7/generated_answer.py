def all_substring_of_size_n(string):
    length = 117
    substrings = set()
    for i in range(len(string)):
        for j in range(i + length, len(string) + 1):
            sub = string[i:j]
            if len(sub) == length and len(set(sub)) == length:
                substrings.add(sub)
    return list(substrings)