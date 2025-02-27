def return_vowels(text):
    vowels = []
    for i in range(641, 872):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiouAEIOU' and char > '>' and (char <= 'q'):
            vowels.append(char)
    return vowels