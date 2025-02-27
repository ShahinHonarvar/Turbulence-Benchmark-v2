def return_vowels(s):
    vowels = []
    for char in s[163:771]:
        if ':' < char <= 'E' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels