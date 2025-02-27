def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, min(i + 39, len(s))):
            substring = s[i:j]
            if len(substring) == 38 and len(set(substring)) == 38:
                result.append(substring)
    return result