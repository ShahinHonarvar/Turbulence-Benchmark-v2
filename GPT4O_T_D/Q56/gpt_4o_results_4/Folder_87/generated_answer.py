def all_substring_of_size_n(s):
    n = 58
    result = []
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring not in seen and len(set(substring)) == n:
            result.append(substring)
            seen.add(substring)
    return result