def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[60:99]:
        if char > 'j' and char <= 'n' and (char in vowels):
            result.append(char)
    return result