def all_substring_of_size_n(s):
    if len(s) < 5:
        return []
    result = set()
    for i in range(len(s)):
        temp_str = ''.join(sorted(s[i:i + 5]))
        if len(temp_str) == 5 and len(set(s[i:i + 5])) == 5:
            result.add(temp_str)
    return list(result)