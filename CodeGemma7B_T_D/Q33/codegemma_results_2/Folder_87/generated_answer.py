def return_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_list = []
    for letter in text[34:58]:
        if letter in vowels and letter > 'b' and (letter <= 'o'):
            vowel_list.append(letter)
    return vowel_list