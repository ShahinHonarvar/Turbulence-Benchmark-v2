def return_vowels(text):
    vowels = []
    for i in range(17, min(len(text), 65)):
        if text[i] in 'AEIOUaeiou' and 'U' < text[i] <= '{':
            vowels.append(text[i])
    return vowels