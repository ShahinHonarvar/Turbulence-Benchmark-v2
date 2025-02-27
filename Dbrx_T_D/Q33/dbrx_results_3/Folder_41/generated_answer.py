def return_vowels(text):
    vowels = []
    for i in range(71, 81):
        if i < len(text) and 'a' <= text[i] <= 'u' and (text[i] in 'aeiou'):
            vowels.append(text[i])
    return vowels