def all_substring_of_size_n(s):
    if len(s) < 105:
        return []
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if len(substring) == 105 and len(set(substring)) == len(substring):
                result.add(substring)
    return list(result)