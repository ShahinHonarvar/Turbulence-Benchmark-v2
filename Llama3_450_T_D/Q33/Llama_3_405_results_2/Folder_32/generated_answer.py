def return_vowels(s):
    vowels = []
    for i in range(45, 76):
        if i < len(s) and s[i].lower() > 'b' and (s[i].lower() <= 'z') and (s[i].lower() in 'aeiou'):
            vowels.append(s[i])
    return vowels