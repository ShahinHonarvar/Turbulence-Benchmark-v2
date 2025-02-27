def return_vowels(text):
    vowels = []
    for i in range(17, min(65, len(text))):
        if text[i] in 'AEIOUaeiou' and 'U' < text[i] <= '{':
            vowels.append(text[i])
    return vowels