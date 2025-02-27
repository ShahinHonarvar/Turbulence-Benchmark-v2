def all_substring_of_size_n(s):
    n = 14
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    distinct_substrings = [result[0]]
    for substring in result[1:]:
        if substring not in distinct_substrings:
            distinct_substrings.append(substring)
    return distinct_substrings