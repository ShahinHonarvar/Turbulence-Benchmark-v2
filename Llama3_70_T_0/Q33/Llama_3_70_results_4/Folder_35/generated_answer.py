def return_vowels(s):
    vowels = []
    for char in s[483:664]:
        if '&' < char <= 'h' and char in 'aeiou':
            vowels.append(char)
    return vowels