def all_substring_of_size_n(s):
    seen = set()
    result = []
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(set(substring)) == 90 and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result