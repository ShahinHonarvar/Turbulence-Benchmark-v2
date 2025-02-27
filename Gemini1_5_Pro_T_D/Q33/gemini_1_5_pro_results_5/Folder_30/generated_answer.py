def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(11, min(61, len(text))):
        char = text[i]
        if char in vowels and char > 'M' and (char <= 'W'):
            result.append(char)
    return result