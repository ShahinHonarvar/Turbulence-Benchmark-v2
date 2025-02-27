def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[495:837]:
        if 'B' < char <= 't' and char in vowels:
            result.append(char)
    return result