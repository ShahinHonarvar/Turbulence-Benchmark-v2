def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for index in range(170, 645):
        if index < len(text):
            char = text[index]
            if char in vowels and 'E' < char <= '~':
                result.append(char)
    return result