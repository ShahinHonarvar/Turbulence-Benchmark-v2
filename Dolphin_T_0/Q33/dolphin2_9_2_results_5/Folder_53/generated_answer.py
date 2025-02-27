def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[27:57]:
        if 'o' < char <= 'w' and char in vowels:
            result.append(char)
    return result