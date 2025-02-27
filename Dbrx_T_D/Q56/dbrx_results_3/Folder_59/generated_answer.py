def all_substring_of_size_n(s):
    result = []
    n = 77
    if len(s) < n:
        return result
    substring = set()
    for i in range(len(s) - n + 1):
        substring.clear()
        for j in range(n):
            substring.add(s[i + j])
        if len(substring) == n:
            result.append(''.join(substring))
    return result