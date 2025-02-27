def all_substring_of_size_n(s):
    results = []
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if len(substring) == len(set(substring)):
            results.append(substring)
    return results