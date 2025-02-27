def return_vowels(txt):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in txt:
        if char.upper() in vowels:
            if ord(char) > ord('?'):
                if ord(char) <= ord('P'):
                    if ord(char) >= 32 and ord(char) <= 61:
                        result.append(char)
    return result