def return_vowels(text):
    vowels = []
    for i in range(328, 455):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiou' and '<' < char <= 'z':
            vowels.append(char)
    return vowels