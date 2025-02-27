def return_vowels(s):
    vowels = []
    for char in s[56:96]:
        if '&' < char <= 'T' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels