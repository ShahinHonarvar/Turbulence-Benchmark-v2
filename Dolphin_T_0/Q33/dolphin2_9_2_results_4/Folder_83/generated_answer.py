def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[90:97]:
        if char in vowels and char >= '_' and (char <= 'x'):
            result.append(char)
    return result