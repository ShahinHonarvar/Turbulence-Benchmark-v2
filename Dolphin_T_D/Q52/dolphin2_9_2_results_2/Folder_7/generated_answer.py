def palindrome_of_length_n(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = set()
    for i in range(len(s) - 415):
        word = s[i:i + 416]
        if all([c in alphabet for c in word]) and word == word[::-1]:
            res.add(word)
    return res