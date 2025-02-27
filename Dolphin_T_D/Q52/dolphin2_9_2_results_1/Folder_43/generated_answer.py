def palindrome_of_length_n(s):
    n = 51
    s = s.lower()
    set_palindrome = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            set_palindrome.add(s[i:i + n])
    return set_palindrome