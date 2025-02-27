def all_substring_of_size_n(s):
    result = []
    length = len(s)
    seen = set()
    for i in range(length - 45):
        substr = s[i:i + 46]
        if len(substr) == 46 and len(set(substr)) == 46 and (substr not in seen):
            seen.add(substr)
            result.append(substr)
    return result