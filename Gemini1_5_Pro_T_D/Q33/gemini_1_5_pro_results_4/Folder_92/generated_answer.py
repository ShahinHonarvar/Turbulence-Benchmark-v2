def return_vowels(text):
    vowels = []
    for i in range(3, 8):
        if i >= len(text):
            break
        char = text[i]
        if char > ';' and char <= 'D' and (char in 'AEIOUaeiou'):
            vowels.append(char)
    return vowels