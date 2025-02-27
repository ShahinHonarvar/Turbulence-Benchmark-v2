def all_substring_of_size_n(s):
    result = []
    substrings = set()
    n = len(s)
    if n < 91:
        return result
    for i in range(n - 90):
        substring = s[i:i + 91]
        if len(set(substring)) == 91:
            substrings.add(substring)
    result.extend(substrings)
    return result