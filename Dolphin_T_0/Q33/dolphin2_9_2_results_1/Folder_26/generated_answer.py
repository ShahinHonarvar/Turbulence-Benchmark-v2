def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[10:82]:
        if char > '$' and char <= '@' and (char in vowels):
            result.append(char)
    return result