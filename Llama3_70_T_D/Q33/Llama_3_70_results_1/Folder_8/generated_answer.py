def return_vowels(s):
    vowels = []
    for char in s[64:82]:
        if char in 'aeiou':
            vowels.append(char)
    return vowels