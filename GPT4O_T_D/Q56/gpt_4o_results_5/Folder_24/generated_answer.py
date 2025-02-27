def all_substring_of_size_n(s):

    def has_no_duplicates(substr):
        return len(set(substr)) == len(substr)
    result = []
    n = 52
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_no_duplicates(substring):
            result.append(substring)
    return result