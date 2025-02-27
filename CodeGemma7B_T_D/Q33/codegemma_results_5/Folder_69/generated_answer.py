def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i, char in enumerate(text):
        if i >= 641 and i < 872 and (char in vowels) and (char > text[i - 1]) and (char <= 'q'):
            filtered_vowels.append(char)
    return filtered_vowels