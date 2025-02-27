def all_substring_of_size_n(s):
    n = 142
    substr = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            temp = s[i:j]
            if len(set(temp)) == n:
                substr.add(temp)
    return list(substr)