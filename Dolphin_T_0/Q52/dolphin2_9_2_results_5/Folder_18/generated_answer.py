def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 392, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and set(sub).issubset(set('abcdefghijklmnopqrstuvwxyz')):
                result.add(sub)
    return result