def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        substring = s[i:i + 47]
        if len(set(substring)) == 47:
            result.add(substring)
    return list(result)