def all_substring_of_size_n(s):
    distinct_substrings = []
    for i in range(len(s) - 31):
        substring = s[i:i + 32]
        if len(set(substring)) == 32:
            distinct_substrings.append(substring)
    return distinct_substrings