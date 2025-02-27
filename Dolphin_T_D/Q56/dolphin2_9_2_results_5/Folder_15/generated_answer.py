def all_substring_of_size_n(s):
    result = set()
    for i in range(0, len(s) - 2):
        sub = s[i:i + 3]
        if len(set(sub)) == 3:
            result.add(sub)
    return list(result)