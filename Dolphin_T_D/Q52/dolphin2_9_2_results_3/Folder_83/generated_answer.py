def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for i in range(length - 23):
        sub = s[i:i + 24]
        if sub == sub[::-1]:
            result.add(sub)
    return result