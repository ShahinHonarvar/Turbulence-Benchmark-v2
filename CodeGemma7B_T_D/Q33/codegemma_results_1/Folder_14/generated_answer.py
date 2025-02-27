def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for idx, char in enumerate(text):
        if idx >= 47 and idx < 61 and (char in vowels) and (ord(char) > 9) and (ord(char) <= ord('O')):
            result.append(char)
    return result