def all_substring_of_size_n(s):

    def has_no_duplicates(substring):
        return len(substring) == len(set(substring))
    substrings = [s[i:i + 96] for i in range(len(s) - 95) if has_no_duplicates(s[i:i + 96])]
    return substrings