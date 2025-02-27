def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 38):
        sub = s[i:i + 39]
        if sub == sub[::-1]:
            result.add(sub)
    return result