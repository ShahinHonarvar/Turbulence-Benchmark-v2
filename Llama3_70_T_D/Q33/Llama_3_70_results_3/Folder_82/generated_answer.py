def return_vowels(s):
    vowels = []
    for char in s[86:100]:
        if 'E' < char <= 'r' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels