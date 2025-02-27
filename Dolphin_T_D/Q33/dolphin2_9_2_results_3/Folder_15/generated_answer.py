def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[5:6]:
        if 3 < ord(char) <= ord('^') and char in vowels:
            result.append(char)
    return result