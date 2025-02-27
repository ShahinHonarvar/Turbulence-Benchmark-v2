def all_substring_of_size_n(s):

    def has_unique_chars(sub):
        return len(set(sub)) == len(sub)
    n = 6
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_unique_chars(substring):
            result.append(substring)
    return result