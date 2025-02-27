def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for character in text[483:664]:
        if '&' < character <= 'h' and character in vowels:
            result.append(character)
    return result