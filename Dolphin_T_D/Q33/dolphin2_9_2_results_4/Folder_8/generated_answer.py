def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[64:82]:
        if 'p' < char <= 'z' and char in vowels:
            result.append(char)
    return result