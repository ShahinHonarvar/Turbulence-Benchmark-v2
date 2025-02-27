def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[142:145]:
        if 4 < ord(char) <= ord('o') and char in vowels:
            result.append(char)
    return result