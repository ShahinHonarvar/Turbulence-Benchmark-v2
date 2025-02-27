def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[51:77]:
        if 4 < ord(char) <= ord('=') and char in vowels:
            result.append(char)
    return result