def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[528:606]:
        if 'm' < char <= 'x':
            if char in vowels:
                result.append(char)
    return result