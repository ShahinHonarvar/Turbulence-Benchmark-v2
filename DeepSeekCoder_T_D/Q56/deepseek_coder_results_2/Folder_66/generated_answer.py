def all_substring_of_size_n(s):

    def is_valid_substring(substring):
        return len(set(substring)) == 26
    result = []
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if is_valid_substring(substring):
            result.append(substring)
    return result