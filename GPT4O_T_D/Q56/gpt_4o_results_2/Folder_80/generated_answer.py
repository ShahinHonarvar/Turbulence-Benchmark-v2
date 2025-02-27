def all_substring_of_size_n(s):

    def is_unique(substring):
        return len(substring) == len(set(substring))
    result = []
    length = len(s)
    for i in range(length - 30):
        substring = s[i:i + 31]
        if is_unique(substring):
            result.append(substring)
    return result