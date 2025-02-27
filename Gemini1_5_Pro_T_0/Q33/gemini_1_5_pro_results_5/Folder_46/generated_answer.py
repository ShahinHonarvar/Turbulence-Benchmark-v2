def return_vowels(text):
    vowels = []
    for i in range(max(10, 0), min(83, len(text))):
        char = text[i]
        if '%' < char <= 'e':
            if char in 'aeiou':
                vowels.append(char)
    return vowels