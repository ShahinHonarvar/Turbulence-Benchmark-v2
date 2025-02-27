def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[528:606]:
        if ord('M') < ord(char) <= ord('X') and char in vowels:
            result.append(char)
    return result