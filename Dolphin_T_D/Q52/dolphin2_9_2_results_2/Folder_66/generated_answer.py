def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 24):
        sub = s[i:i + 25]
        if sub == sub[::-1]:
            result.add(sub)
    return result