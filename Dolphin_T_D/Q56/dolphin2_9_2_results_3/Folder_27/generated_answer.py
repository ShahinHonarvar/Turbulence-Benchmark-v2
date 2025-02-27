def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 56):
        sub = string[i:i + 57]
        if len(set(sub)) == 57:
            substrings.add(sub)
    return list(substrings)