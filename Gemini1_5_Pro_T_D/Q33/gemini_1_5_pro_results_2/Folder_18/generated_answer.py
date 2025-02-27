def return_vowels(text):
    vowels = []
    for i in range(528, 606):
        if i < len(text):
            char = text[i]
            if char in 'AEIOUaeiou' and 'M' < char <= 'X':
                vowels.append(char)
    return vowels