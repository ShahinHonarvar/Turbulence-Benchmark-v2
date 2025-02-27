def return_vowels(text):
    vowels = []
    for i in range(260, 322):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > '%' and (char <= 'U'):
                vowels.append(char)
    return vowels