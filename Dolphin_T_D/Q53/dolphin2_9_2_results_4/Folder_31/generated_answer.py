def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 33):
        for j in range(i + 34, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                result.add(sub)
    return result