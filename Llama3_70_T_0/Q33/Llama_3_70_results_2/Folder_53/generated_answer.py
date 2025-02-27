def return_vowels(s):
    vowels = []
    for char in s[27:57]:
        if 'o' < char <= 'w' and char in 'aeiou':
            vowels.append(char)
    return vowels