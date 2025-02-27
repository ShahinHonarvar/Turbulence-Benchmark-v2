def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = 255
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub == sub[::-1]:
            result.add(sub)
    return result