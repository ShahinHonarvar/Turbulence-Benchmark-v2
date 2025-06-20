def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(14, len(s) + 1):
        if s[:i] == s[::-1][:i]:
            res.add(s[:i])
    return res