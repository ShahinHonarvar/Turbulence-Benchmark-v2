def all_substring_of_size_n(s):
    result = set()
    length = 60
    for i in range(len(s)):
        substring = s[i:i + length]
        if len(substring) == length:
            if len(set(substring)) == length:
                result.add(substring)
    return list(result)