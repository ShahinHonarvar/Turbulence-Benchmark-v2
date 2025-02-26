def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(529, 828):
        if i < len(text):
            char = text[i]
            if char in vowels and 'U' < char <= 'l':
                result.append(char)
    return result