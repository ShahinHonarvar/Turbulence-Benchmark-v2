def all_substring_of_size_n(s):
    if len(s) < 88:
        return []
    substrings = [s[i:i + 88] for i in range(len(s) - 87)]
    unique_substrings = list(set(substrings))
    substrings_no_duplicates = [s for s in unique_substrings if len(set(s)) == 88]
    return substrings_no_duplicates