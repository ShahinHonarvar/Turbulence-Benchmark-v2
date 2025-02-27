def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[40:94]:
        if 4 < ord(char) <= ord('H') and char in vowels:
            result.append(char)
    return result