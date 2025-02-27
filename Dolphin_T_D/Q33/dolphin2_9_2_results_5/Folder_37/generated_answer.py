def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[82:90]:
        if char > 'T' and char <= 'b' and (char in vowels):
            result.append(char)
    return result