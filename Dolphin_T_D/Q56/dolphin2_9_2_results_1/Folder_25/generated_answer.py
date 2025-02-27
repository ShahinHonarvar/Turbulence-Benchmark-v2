def all_substring_of_size_n(string):
    if len(string) < 67:
        return []
    substrings = []
    i = 0
    while i + 67 <= len(string):
        piece = string[i:i + 67]
        if len(set(piece)) == len(piece):
            substrings.append(piece)
        i += 1
    return substrings