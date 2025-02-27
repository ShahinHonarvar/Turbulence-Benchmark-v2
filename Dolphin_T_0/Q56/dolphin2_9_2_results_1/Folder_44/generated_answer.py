def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i + 90, n):
            substring = s[i:j]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    distinct_substrings = list(set(substrings))
    return distinct_substrings