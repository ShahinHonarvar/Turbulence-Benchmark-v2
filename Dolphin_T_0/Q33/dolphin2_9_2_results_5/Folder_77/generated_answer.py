def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [text[i] for i in range(837, 975) if text[i] in vowels and text[i] > 'n' and (text[i] <= 'w')]