def palindrome_of_length_at_least_n(s):
    result = set()
    n = len(s)
    s = s.lower()
    for i in range(n):
        for j in range(i + 72, n):
            sub = s[i:j + 1]
            if sub == sub[::-1] and all((c for c in sub if c.isalpha())):
                result.add(sub)
    return result