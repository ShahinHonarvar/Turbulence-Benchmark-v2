def return_vowels(text):
    vowels = []
    for i in range(604, 949):
        if i < len(text) and 'N' < text[i] <= 'U' and (text[i] in 'AEIOU'):
            vowels.append(text[i])
    return vowels