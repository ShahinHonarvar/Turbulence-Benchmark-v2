def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 144, len(s) + 1):
            t = s[i:j]
            if t.isalpha() and t == t[::-1]:
                result.add(t)
    return result