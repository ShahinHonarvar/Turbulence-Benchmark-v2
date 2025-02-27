def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 406):
        sub = s[i:i + 407]
        if all((c.isalpha() for c in sub)) and sub == sub[::-1]:
            result.add(sub)
    return result