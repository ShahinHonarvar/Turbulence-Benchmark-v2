def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(set(substring)) == 98:
            unique_substrings.add(substring)
    return list(unique_substrings)