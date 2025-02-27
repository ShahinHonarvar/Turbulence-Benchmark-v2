def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in string:
        if 65 <= ord(char) < 70 and char in vowels:
            result.append(char)
    return result