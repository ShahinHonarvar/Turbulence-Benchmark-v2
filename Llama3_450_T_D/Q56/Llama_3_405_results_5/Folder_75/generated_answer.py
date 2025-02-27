def all_substring_of_size_n(s):

    def has_no_duplicate_chars(substring):
        return len(set(substring)) == len(substring)
    substrings = [s[i:i + 16] for i in range(len(s) - 15) if has_no_duplicate_chars(s[i:i + 16])]
    return list(set(substrings))