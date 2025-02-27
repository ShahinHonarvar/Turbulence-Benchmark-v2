def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 54, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 54 and len(set(substring)) == 54:
                result.add(substring)
    return list(result)