def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 45):
        sub = s[i:i + 46]
        if sub == sub[::-1]:
            result.add(sub)
    return result