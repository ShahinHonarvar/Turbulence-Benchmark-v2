def return_vowels(s):
    vowels = []
    for char in s[32:97]:
        if 'Q' < char <= ']' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels