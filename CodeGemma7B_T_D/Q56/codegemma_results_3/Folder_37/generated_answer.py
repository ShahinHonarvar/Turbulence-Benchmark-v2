def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 65, len(s)):
            substring = s[i:j]
            if len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)