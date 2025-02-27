def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if j - i + 1 >= 81:
                sub = s[i:j]
                if sub == sub[::-1]:
                    result.add(sub)
    return result