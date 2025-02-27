def all_substring_of_size_n(s):
    results = []
    length = len(s)
    for i in range(length - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            results.append(substring)
    return results