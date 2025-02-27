def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 400):
        sub = s[i:i + 401]
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result