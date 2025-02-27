def return_vowels(s):
    vowels = []
    for char in s[22:82]:
        if 'N' < char <= 'o' and char in 'aeiou':
            vowels.append(char)
    return vowels