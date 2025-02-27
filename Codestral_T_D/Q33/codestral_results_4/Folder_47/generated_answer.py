def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:38]:
        if char > 'N' and char <= 'k':
            if char.lower() in vowels:
                result.append(char)
    return result