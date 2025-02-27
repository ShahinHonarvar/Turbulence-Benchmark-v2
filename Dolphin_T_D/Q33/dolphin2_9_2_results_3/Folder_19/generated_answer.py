def return_vowels(s):
    v = []
    for i in range(51, 77):
        if 'a' <= s[i] <= '=' and s[i] != ' ' and (s[i] != 'c'):
            v.append(s[i])
    return v