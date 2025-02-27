def all_substring_of_size_n(s):
    if len(s) < 42:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if len(substring) == len(set(substring)):
            if substring not in seen:
                result.append(substring)
                seen.add(substring)
    return result