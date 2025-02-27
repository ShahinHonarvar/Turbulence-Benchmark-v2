def all_substring_of_size_n(s):
    results = []
    length = len(s)
    for i in range(length - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16:
            results.append(substring)
    return list(set(results))