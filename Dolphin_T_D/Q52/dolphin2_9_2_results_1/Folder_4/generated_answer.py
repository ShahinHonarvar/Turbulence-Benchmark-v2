def palindrome_of_length_n(s):
    s = s.lower()
    pals = set()
    for i in range(len(s) - 14):
        if s[i:i + 15] == s[i:i + 15][::-1]:
            pals.add(s[i:i + 15])
    return pals