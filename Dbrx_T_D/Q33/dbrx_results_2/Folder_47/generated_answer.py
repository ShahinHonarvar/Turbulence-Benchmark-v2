def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:38]:
        if char > 'N' and char <= 'k' and (char in vowels):
            result.append(char)
    return result