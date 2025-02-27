def return_vowels(s):
    vowels = []
    for i in range(47, 61):
        if 'a' <= s[i] <= 'z' and s[i] in 'aeiou' and (s[i] > chr(9)) and (s[i] <= 'O'):
            vowels.append(s[i])
    return vowels