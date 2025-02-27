def all_substring_of_size_n(s):

    def has_unique_characters(substring):
        return len(set(substring)) == len(substring)
    if len(s) < 54:
        return []
    substrings = []
    for i in range(len(s) - 53):
        sub = s[i:i + 54]
        if has_unique_characters(sub):
            substrings.append(sub)
    return list(set(substrings))