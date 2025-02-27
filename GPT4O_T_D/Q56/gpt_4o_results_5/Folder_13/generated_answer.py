def all_substring_of_size_n(s):

    def is_unique_chars(substr):
        return len(substr) == len(set(substr))
    result = []
    for i in range(len(s) - 53 + 1):
        substring = s[i:i + 53]
        if is_unique_chars(substring):
            result.append(substring)
    return result