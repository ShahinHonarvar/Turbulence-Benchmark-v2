def return_vowels(text):
    vowels = []
    for i in range(17, 65):
        if i < len(text) and 'U' < text[i] <= '{':
            if text[i] in 'AEIOUaeiou':
                vowels.append(text[i])
    return vowels