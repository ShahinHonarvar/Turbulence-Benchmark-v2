def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in s:
        if 32 <= ord(char) < 61 and char > '?' and (char <= 'P') and (char in vowels):
            result.append(char)
    return result