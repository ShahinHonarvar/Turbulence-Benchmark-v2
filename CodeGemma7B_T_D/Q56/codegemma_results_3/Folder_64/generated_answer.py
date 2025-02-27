def all_substring_of_size_n(s):
    seen = set()
    for i in range(len(s) - 7):
        substring = s[i:i + 8]
        if substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result