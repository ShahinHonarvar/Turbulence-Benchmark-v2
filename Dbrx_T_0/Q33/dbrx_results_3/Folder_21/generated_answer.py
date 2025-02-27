def return_vowels(s):
    vowels = []
    for i in range(464, 574):
        if s[i] > 'a' and s[i] <= 'g' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels