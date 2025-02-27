def return_vowels(s):
    vowels = []
    for char in s[3:9]:
        if 'S' < char <= 'U' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels