def return_vowels(s):
    vowels = []
    for i in range(28, 76):
        char = s[i]
        if char.isalpha() and char.lower() in 'aeiou' and ('+' < char < 'z'):
            vowels.append(char)
    return vowels