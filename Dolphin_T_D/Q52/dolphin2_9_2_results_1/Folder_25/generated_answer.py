def palindrome_of_length_n(s):
    n = 90
    s = s.lower()
    set_palindrome = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            set_palindrome.add(sub)
    return set_palindrome