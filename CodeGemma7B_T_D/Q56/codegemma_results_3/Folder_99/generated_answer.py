def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if len(substring) == 110 and len(set(substring)) == len(substring):
                result.add(substring)
    return list(result)