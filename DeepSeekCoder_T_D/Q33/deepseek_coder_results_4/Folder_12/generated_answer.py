def return_vowels(s):
    vowels = []
    for char in s[13:37]:
        if 'Z' < char <= '}' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels