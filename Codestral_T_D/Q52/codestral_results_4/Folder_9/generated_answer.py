def palindrome_of_length_n(s):
    s = s.lower()
    length = 72
    result = set()
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result