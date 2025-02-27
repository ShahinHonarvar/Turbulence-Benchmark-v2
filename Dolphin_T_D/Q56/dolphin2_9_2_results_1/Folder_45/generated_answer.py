def all_substring_of_size_n(string):
    size = 29
    substrings = []
    if len(string) < size:
        return []
    while size <= len(string):
        for i in range(len(string)):
            sub = string[i:i + size]
            if len(set(sub)) == size and sub not in substrings:
                substrings.append(sub)
        size -= 1
    return substrings