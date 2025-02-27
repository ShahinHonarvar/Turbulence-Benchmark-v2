def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(set(substring)) == 98 and substring not in substrings:
            substrings.add(substring)
    return list(substrings)