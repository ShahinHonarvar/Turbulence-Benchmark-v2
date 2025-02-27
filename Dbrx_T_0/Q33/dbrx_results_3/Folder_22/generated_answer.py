def return_vowels(s):
    vowels = []
    for i in range(56, 90):
        if s[i].lower() > 'k' and s[i].lower() <= 'z' and (s[i].lower() in 'aeiou'):
            vowels.append(s[i])
    return vowels