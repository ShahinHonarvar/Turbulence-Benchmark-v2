def return_vowels(text):
    vowels = []
    for i in range(17, min(65, len(text))):
        char = text[i]
        if char in 'AEIOaeio' and 'U' < char <= '{':
            vowels.append(char)
    return vowels