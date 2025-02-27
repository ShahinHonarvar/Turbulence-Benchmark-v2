def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[41:50]:
        if char > 'W' and char <= '[' and (char in vowels):
            result.append(char)
    return result