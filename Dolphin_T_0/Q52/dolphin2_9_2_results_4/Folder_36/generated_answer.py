def palindrome_of_length_n(s):
    s = s.lower()
    set_palindrome = set()
    for i in range(len(s) - 337):
        sub = s[i:i + 338]
        if sub == sub[::-1]:
            set_palindrome.add(sub)
    return set_palindrome