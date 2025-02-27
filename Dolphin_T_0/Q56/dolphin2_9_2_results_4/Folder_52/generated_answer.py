def all_substring_of_size_n(s):
    length = len(s)
    result = []
    if length < 15:
        return result
    distinct_chars = set(s)
    if len(distinct_chars) < 15:
        return result
    for i in range(length - 15 + 1):
        substring = s[i:i + 15]
        if len(set(substring)) == 15:
            if substring not in result:
                result.append(substring)
    return result