def return_vowels(text):
    vowels = []
    for char in text[0:87]:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(char)
            if len(vowels) == 11:
                break
    return vowels