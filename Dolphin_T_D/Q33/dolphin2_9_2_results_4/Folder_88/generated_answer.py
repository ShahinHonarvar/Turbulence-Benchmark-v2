def return_vowels(s):
    vowels = []
    for i in range(70, 76):
        if ord('a') <= ord(s[i]) <= ord('z') and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels