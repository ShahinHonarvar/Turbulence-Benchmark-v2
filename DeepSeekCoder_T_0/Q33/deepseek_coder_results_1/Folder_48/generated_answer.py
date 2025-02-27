def return_vowels(s):
    vowels = []
    for char in s[529:828]:
        if 'U' < char <= 'l' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels