def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string:
        if ord(char) > ord('Q') and ord(char) <= ord(']') and (char in vowels) and (ord(char) >= 32) and (ord(char) < 97):
            result.append(char)
    return result