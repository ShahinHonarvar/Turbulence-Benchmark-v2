def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[13:35]:
        if char.lower() in vowels and 8 < ord(char.lower()) <= ord('f'):
            result.append(char)
    return result