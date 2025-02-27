def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            word = s[i:j]
            if word == word[::-1] and len(word) >= 84:
                res.add(word)
    return res