def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 5, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                result.add(sub)
    return result