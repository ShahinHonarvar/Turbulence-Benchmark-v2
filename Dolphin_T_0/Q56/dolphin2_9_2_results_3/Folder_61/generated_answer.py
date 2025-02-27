def all_substring_of_size_n(s):
    n = 39
    output = set()
    for i in range(0, len(s) - n + 1):
        t = s[i:i + n]
        if len(set(t)) == n:
            output.add(t)
    return list(output)