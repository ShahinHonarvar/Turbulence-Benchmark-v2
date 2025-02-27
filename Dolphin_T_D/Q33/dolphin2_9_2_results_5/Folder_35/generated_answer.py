def return_vowels(text):
    vowels = 'aeiou'
    list_vowels = []
    for char in text[483:664]:
        if '&' < char <= 'h' and char in vowels:
            list_vowels.append(char)
    return list_vowels