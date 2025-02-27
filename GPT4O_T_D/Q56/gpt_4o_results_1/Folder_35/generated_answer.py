def all_substring_of_size_n(s):
    n = 27
    result = []
    substrings_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in substrings_set:
            result.append(substring)
            substrings_set.add(substring)
    return result