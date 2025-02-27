def return_vowels(text):
    vowels = 'aeiou'
    result = []
    for char in text[32:97]:
        if char > 'Q' and char <= ']':
            if char in vowels:
                result.append(char)
    return result