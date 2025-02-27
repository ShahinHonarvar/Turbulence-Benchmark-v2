def palindrome_of_length_n(s):
    result = set()
    n = 91
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result