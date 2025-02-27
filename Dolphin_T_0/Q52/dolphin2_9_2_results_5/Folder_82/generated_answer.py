def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 27):
        sub = s[i:i + 28]
        if sub == sub[::-1] and all((char.isalpha() for char in sub)):
            result.add(sub)
    return result