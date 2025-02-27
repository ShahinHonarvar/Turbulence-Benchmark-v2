def all_substring_of_size_n(s):

    def is_valid(substring):
        return len(substring) == len(set(substring))
    result = []
    for i in range(len(s) - 7):
        substring = s[i:i + 8]
        if is_valid(substring):
            result.append(substring)
    return result