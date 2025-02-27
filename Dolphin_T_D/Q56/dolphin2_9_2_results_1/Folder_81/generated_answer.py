def all_substring_of_size_n(s):
    if len(s) < 98:
        return []
    else:
        substrings = set()
        for i in range(len(s) - 97):
            substr = s[i:i + 98]
            if len(set(substr)) == 98:
                substrings.add(substr)
        return list(substrings)