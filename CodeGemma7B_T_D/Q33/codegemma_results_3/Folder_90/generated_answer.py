def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    extracted_vowels = []
    for i in range(142, 145):
        letter = text[i]
        if letter in vowels and 4 < ord(letter) <= ord('o'):
            extracted_vowels.append(letter)
    return extracted_vowels