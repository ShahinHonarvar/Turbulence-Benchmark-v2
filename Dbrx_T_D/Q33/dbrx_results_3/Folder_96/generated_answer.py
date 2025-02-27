def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[77:84]:
        if char.lower() in vowels and (char > '(' and char <= 'G'):
            result.append(char)
    return result