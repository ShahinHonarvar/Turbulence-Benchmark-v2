import string

def palindrome_of_length_n(s):
    s = s.lower()
    letters = set(string.ascii_lowercase)
    pals = set()
    length = 73
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1 - length):
            sub = s[i:j]
            if sub == sub[::-1] and set(sub).issubset(letters):
                pals.add(sub)
    return pals