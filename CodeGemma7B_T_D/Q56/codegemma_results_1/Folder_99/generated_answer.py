def all_substring_of_size_n(s):
    results = []
    size_n = 110
    for i in range(len(s)):
        for j in range(i + size_n - 1, len(s)):
            substring = s[i:j + 1]
            if len(substring) == size_n and len(set(substring)) == size_n:
                results.append(substring)
    return results