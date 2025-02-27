def return_vowels(s):
    vowels = []
    for char in s[40:91]:
        if char.lower() in 'aeiou' and 'A' < char <= 'x':
            vowels.append(char)
    return vowels