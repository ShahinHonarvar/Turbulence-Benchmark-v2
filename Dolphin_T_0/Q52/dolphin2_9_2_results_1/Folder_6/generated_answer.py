def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 473, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                result.add(sub)
    return result