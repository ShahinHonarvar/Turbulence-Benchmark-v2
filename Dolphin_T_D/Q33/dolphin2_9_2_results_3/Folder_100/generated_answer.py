def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:75]:
        if char > 'L' and char <= 'd':
            if char in vowels:
                result.append(char)
    return result