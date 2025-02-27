def all_substring_of_size_n(s):
    substr = set()
    for i in range(len(s) - 97):
        if len(set(s[i:i + 98])) == 98:
            substr.add(s[i:i + 98])
    return list(substr)