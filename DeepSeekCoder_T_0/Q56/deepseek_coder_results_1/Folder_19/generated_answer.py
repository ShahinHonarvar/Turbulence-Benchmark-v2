def all_substring_of_size_n(s):

    def has_unique_chars(substring):
        return len(set(substring)) == len(substring)
    substrings = []
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if has_unique_chars(substring):
            substrings.append(substring)
    return substrings