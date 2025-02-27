def all_substring_of_size_n(s):

    def is_substring_valid(substring):
        return len(substring) == len(set(substring)) == 12
    result = []
    for i in range(len(s)):
        for j in range(i + 12, len(s) + 1):
            substring = s[i:j]
            if is_substring_valid(substring):
                result.append(substring)
    return result