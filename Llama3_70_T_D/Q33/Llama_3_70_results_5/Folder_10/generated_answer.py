def return_vowels(s):
    vowels = []
    for char in s[31:37]:
        if ';' < char <= 't' and char in 'aeiou':
            vowels.append(char)
    return vowels