def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    substring = string[528:606]
    result = []
    for char in substring:
        if char in vowels and ord(char) > ord('M') and (ord(char) <= ord('X')):
            result.append(char)
    return result