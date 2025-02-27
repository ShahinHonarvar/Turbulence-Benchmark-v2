def return_vowels(text):
    vowels = []
    for i in range(17, 65):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > 'U' and (char <= '{'):
                vowels.append(char)
    return vowels