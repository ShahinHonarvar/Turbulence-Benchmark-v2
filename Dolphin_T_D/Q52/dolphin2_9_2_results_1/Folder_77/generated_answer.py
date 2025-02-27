def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 173, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result