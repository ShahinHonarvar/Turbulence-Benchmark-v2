def return_vowels(s):
    vowels = []
    for i in range(24, 68):
        if i < len(s) and s[i].lower() in 'aeiou' and ('f' < s[i] <= '|'):
            vowels.append(s[i])
    return vowels