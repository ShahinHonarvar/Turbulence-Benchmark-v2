def return_vowels(text):
    vowels = []
    for i in range(5, 6):
        if i >= ord('3') and i <= ord('^'):
            if text[i] in 'aeiouAEIOU':
                vowels.append(text[i])
    return vowels