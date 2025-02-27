def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 7):
        if len(set(s[i:i + 88])) == 88:
            result.add(s[i:i + 88])
    return list(result)