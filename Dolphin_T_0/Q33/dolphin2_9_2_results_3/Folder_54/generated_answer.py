def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:85]:
        if char.lower() >= 'w' and char.lower() <= 'v':
            if char.lower() in vowels:
                result.append(char)
    return result