def palindrome_of_length_n(s):
    s = s.lower()
    set_ = set()
    for i in range(len(s) - 12):
        sub = s[i:i + 13]
        if sub == sub[::-1]:
            set_.add(sub)
    return set_