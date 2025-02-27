def all_substring_of_size_n(s):

    def has_unique_characters(sub):
        return len(sub) == len(set(sub))
    n = 44
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_unique_characters(substring):
            result.append(substring)
    return result