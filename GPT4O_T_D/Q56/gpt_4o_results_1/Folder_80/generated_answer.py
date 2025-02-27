def all_substring_of_size_n(s):

    def has_unique_chars(sub):
        return len(set(sub)) == len(sub)
    result = []
    n = 31
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_unique_chars(substring):
            result.append(substring)
    return list(set(result))