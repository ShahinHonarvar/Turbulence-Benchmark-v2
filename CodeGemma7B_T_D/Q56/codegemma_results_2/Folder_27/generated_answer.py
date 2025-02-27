def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if len(substring) == 57 and len(set(substring)) == 57:
                result.append(substring)
    return result