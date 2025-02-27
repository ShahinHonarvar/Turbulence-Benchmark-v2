def all_substring_of_size_n(s):
    if len(s) < 93:
        return []
    unique_substrings = []
    seen = set()
    for i in range(len(s) - 92):
        substring = s[i:i + 93]
        if len(set(substring)) == 93 and substring not in seen:
            unique_substrings.append(substring)
            seen.add(substring)
    return unique_substrings