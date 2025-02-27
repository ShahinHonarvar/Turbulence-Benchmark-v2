def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 79, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == 79:
                result.append(substring)
    return result