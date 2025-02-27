def return_vowels(s):
    vowels = []
    for char in s[273:276]:
        if '+' < char <= 'o' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels