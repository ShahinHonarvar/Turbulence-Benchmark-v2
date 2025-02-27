def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i, char in enumerate(text):
        if i >= 19 and i < 20 and (char in vowels) and (char > '<') and (char <= 'p'):
            result.append(char)
    return result