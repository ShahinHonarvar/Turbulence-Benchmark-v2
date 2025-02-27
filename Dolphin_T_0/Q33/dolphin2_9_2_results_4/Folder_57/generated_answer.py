def return_vowels(s):
    vowels = []
    for i in range(21, 23):
        if 'a' <= s[i] <= 'n':
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(s[i])
    return vowels