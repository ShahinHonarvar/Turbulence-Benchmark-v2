def all_substring_of_size_n(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if len(s) - i + 1 >= 61:
            substring = s[i:i + 61]
            if substring not in seen:
                result.append(substring)
                seen.add(substring)
    return result