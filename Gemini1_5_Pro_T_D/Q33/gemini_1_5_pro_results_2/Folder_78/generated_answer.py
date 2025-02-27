def return_vowels(text):
    vowels = []
    for i in range(46, 90):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and '@' < char <= '[':
                vowels.append(char)
    return vowels