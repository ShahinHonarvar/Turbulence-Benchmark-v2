def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[59:61]:
        if char.isalpha() and char.lower() in vowels and (char <= 'h'):
            result.append(char)
    return result