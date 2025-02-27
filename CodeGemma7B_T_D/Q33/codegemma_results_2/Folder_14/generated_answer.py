def return_vowels(text):
    specified_vowels = list('AEIOUY')
    vowels = []
    for char in text[47:61]:
        if char in specified_vowels and char > '9' and (char <= 'O'):
            vowels.append(char)
    return vowels or []