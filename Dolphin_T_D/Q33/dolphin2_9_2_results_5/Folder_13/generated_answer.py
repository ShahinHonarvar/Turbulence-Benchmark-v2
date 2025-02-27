def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[149:313]:
        if char > 'M' and char <= 'j':
            if char in vowels:
                result.append(char)
    return result