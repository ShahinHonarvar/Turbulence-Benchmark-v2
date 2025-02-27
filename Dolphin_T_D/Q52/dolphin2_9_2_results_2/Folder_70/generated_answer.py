def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 400):
        sub = s[i:i + 401]
        if sub == sub[::-1]:
            result.add(sub)
    return result