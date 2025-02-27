def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[24:64]:
        if 'f' < char <= 'h' and char in vowels:
            result.append(char)
    return result