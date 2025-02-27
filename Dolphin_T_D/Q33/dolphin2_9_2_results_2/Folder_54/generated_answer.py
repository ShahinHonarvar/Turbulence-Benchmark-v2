def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:85]:
        if 'w' < char <= 'v' and char in vowels:
            result.append(char)
    return result