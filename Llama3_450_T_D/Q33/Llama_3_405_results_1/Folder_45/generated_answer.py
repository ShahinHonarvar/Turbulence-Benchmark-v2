def return_vowels(s):
    vowels = []
    for i in range(43, 70):
        if i < len(s) and s[i] > '*' and (s[i] <= 'b') and (s[i].lower() in 'aeiou'):
            vowels.append(s[i])
    return vowels